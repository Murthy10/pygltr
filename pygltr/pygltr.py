import csv
import requests
import argparse


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
        user, project, issues = self()

        with open(file_name, 'w') as csv_file:
            fieldnames = ['id', 'issue', 'milestone', 'estimate', 'spent']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for issue in issues:
                writer.writerow(row(issue))


def row(issue):
    try:
        milestone = issue['milestone']['title']
    except Exception:
        milestone = ''
    try:
        time_estimate = issue['time_stats']['time_estimate']
        total_time_spent = issue['time_stats']['total_time_spent']
    except Exception:
        time_estimate, total_time_spent = 0
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
    parser.add_argument(
        '-f',
        '--file',
        dest='file',
        help='CSV output filename')

    parser.set_defaults(url='https://gitlab.com/api/v4/', file='issues.csv')
    args = parser.parse_args()

    pygltr = PyGltr(url=args.url, token=args.token, project_name=args.project)
    pygltr.to_csv(file_name=args.file)


if __name__ == "__main__":
    main_function()
