import csv
import requests
import argparse
from datetime import timedelta


class PyGltr:
    def __init__(self, url, token, project_name):
        self.headers = {'PRIVATE-TOKEN': token}
        self.url = url
        self.project_name = project_name

    def __call__(self, *args, **kwargs):
        user = self.get_user()
        project = self.get_project(user=user)
        issues = self.get_issues(project=project)
        return user, project, issues

    def get_user(self):
        user_request = requests.get(self.url + 'user', headers=self.headers)
        return user_request.json()

    def get_project(self, user):
        project_request = requests.get(self.url + 'users/{0}/projects?search={1}'.format(user['id'], self.project_name),
                                       headers=self.headers)
        projects = project_request.json()
        assert len(projects) == 1, 'Project {0} not found.'.format(self.project_name)
        return projects[0]

    def get_issues(self, project):
        issues_request = requests.get(self.url + '/projects/{0}/issues'.format(project['id']), headers=self.headers)
        return issues_request.json()

    def to_csv(self, file_name):
        _, _, issues = self()

        with open(file_name, 'w') as csv_file:
            fieldnames = ['id', 'issue', 'milestone', 'estimate', 'spent']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            [writer.writerow(row(issue)) for issue in issues]

    def to_shell(self):
        _, _, issues = self()
        rows = [row(issue) for issue in issues]
        milestones = {}
        for r in rows:
            milestone = r['milestone'].replace(" ", "_")
            if milestone not in milestones:
                milestones[milestone] = {}
                milestones[milestone]['estimate'] = r['estimate']
                milestones[milestone]['spent'] = r['spent']
            else:
                milestones[milestone]['estimate'] += r['estimate']
                milestones[milestone]['spent'] += r['spent']
        [print('{0}  estimate: {1}  spent: {2}'.format(key, timedelta(seconds=milestones[key]['estimate']),
                                                       timedelta(seconds=milestones[key]['spent'])))
         for key in milestones]


def row(issue):
    try:
        milestone = issue['milestone']['title']
    except Exception:
        milestone = '-'
    try:
        time_estimate = issue['time_stats']['time_estimate']
        total_time_spent = issue['time_stats']['total_time_spent']
    except Exception:
        time_estimate, total_time_spent = 0, 0
    return {'id': issue['iid'], 'issue': issue['title'], 'milestone': milestone, 'estimate': time_estimate,
            'spent': total_time_spent}


def main_function():
    parser = argparse.ArgumentParser(description='Get time tracking data from GitLab', )
    parser.add_argument(
        '-t',
        '--token',
        dest='token',
        help='Private GitLab token',
        required=True)
    parser.add_argument(
        '-p',
        '--project',
        dest='project',
        help='Project name',
        required=True)
    parser.add_argument(
        '-u',
        '--url',
        dest='url',
        help='URL of the GitLab API')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-f',
        '--file',
        dest='file',
        help='CSV output filename')
    group.add_argument(
        '-s',
        '--shell',
        dest='shell',
        action='store_true',
        help='Over')
    group.set_defaults(shell=False, file='issues.csv')
    parser.set_defaults(url='https://gitlab.com/api/v4/')
    args = parser.parse_args()
    pygltr = PyGltr(url=args.url, token=args.token, project_name=args.project)
    if args.shell:
        pygltr.to_shell()
    else:
        pygltr.to_csv(file_name=args.file)


if __name__ == "__main__":
    main_function()
