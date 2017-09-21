import csv
import requests
import argparse
from collections import namedtuple

User = namedtuple('User', ['id', 'name', 'username'])
Project = namedtuple('Project', ['id', 'description', 'name'])
Issue = namedtuple('Issue', ['id', 'iid', 'title', 'milestone', 'project_id', 'estimate', 'spent'])


class Gltr:
    def __init__(self, url, token, project):
        self.headers = {'PRIVATE-TOKEN': token}
        self.url = url
        self.project = project

    def __call__(self, *args, **kwargs):
        user = self.get_user()
        project = self.get_project(user=user)
        issues = self.get_issues(project=project)
        return user, project, issues

    def get_user(self):
        user_request = requests.get(self.url + 'user', headers=self.headers)
        user_json = user_request.json()
        return User(name=user_json['name'], id=user_json['id'], username=user_json['username'])

    def get_project(self, user):
        project_request = requests.get(self.url + 'users/{0}/projects?search={1}'.format(user.id, self.project),
                                       headers=self.headers)
        project_json = project_request.json()[0]
        return Project(name=project_json['name'], id=project_json['id'], description=project_json['description'])

    def get_issues(self, project):
        issues_request = requests.get(self.url + '/projects/{0}/issues'.format(project.id), headers=self.headers)
        issues_json = issues_request.json()
        issues = []
        for issue in issues_json:
            milestone = 'None' if issue['milestone']['title'] is None else issue['milestone']['title']
            time_estimate = 0 if issue['time_stats']['time_estimate'] is None else issue['time_stats']['time_estimate']
            total_time_spent = 0 if issue['time_stats']['total_time_spent'] is None else issue['time_stats'][
                'total_time_spent']
            issues.append(Issue(id=issue['id'], iid=issue['iid'], title=issue['title'], milestone=milestone,
                                project_id=project.id, estimate=time_estimate, spent=total_time_spent))
        return issues

    def to_csv(self, file_name):
        user, project, issues = self()

        with open(file_name, 'w') as csv_file:
            fieldnames = ['id', 'issue', 'milestone', 'estimate', 'spent']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for issue in issues:
                writer.writerow({'id': issue.iid, 'issue': issue.title, 'milestone': issue.milestone,
                                 'estimate': issue.estimate, 'spent': issue.spent})


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

    parser.set_defaults(url='https://gitlab.com/api/v4/', file='gltr.csv')
    args = parser.parse_args()

    gltr = Gltr(url=args.url, token=args.token, project=args.project)
    gltr.to_csv(file_name=args.file)


if __name__ == "__main__":
    main_function()
