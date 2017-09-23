import pytest


@pytest.fixture(scope="session", autouse=True)
def issues():
    return [
        {'web_url': 'https://gitlab.com/Murthy10/ranck/issues/14', 'iid': 14, 'created_at': '2017-09-22T18:38:13.034Z',
         'assignee': None, 'title': 'inform on Kalman filter', 'confidential': False, 'state': 'opened',
         'project_id': 4162828, 'description': None, 'labels': ['To Do', 'inform'],
         'updated_at': '2017-09-22T18:40:03.199Z', 'user_notes_count': 0, 'due_date': None,
         'time_stats': {'human_total_time_spent': None, 'total_time_spent': 0, 'human_time_estimate': '3h',
                        'time_estimate': 10800}, 'assignees': [], 'id': 6922461, 'downvotes': 0,
         'author': {'web_url': 'https://gitlab.com/Murthy10', 'state': 'active', 'name': 'Samuel Kurath',
                    'avatar_url': 'https://gitlab.com/uploads/-/system/user/avatar/1148466/avatar.png', 'id': 1148466,
                    'username': 'Murthy10'},
         'milestone': {'iid': 1, 'due_date': '2017-09-26', 'start_date': '2017-09-18',
                       'updated_at': '2017-09-20T16:02:13.637Z', 'title': 'Project setup', 'id': 378341,
                       'project_id': 4162828,
                       'description': 'Initialize the project and setup a suitable project environment.',
                       'state': 'active', 'created_at': '2017-09-20T16:01:19.687Z'}, 'weight': None, 'upvotes': 0},
        {'web_url': 'https://gitlab.com/Murthy10/ranck/issues/13', 'iid': 13, 'created_at': '2017-09-21T14:45:28.615Z',
         'assignee': {'web_url': 'https://gitlab.com/Murthy10', 'state': 'active', 'name': 'Samuel Kurath',
                      'avatar_url': 'https://gitlab.com/uploads/-/system/user/avatar/1148466/avatar.png', 'id': 1148466,
                      'username': 'Murthy10'}, 'title': 'Prepare time reports', 'confidential': False,
         'state': 'opened', 'project_id': 4162828, 'description': 'Use the Gitlab API for time reports',
         'labels': ['Doing'], 'updated_at': '2017-09-21T19:22:52.471Z', 'user_notes_count': 0, 'due_date': None,
         'time_stats': {'human_total_time_spent': '1d', 'total_time_spent': 28800, 'human_time_estimate': '1d',
                        'time_estimate': 28800}, 'assignees': [
            {'web_url': 'https://gitlab.com/Murthy10', 'state': 'active', 'name': 'Samuel Kurath',
             'avatar_url': 'https://gitlab.com/uploads/-/system/user/avatar/1148466/avatar.png', 'id': 1148466,
             'username': 'Murthy10'}], 'id': 6907199, 'downvotes': 0,
         'author': {'web_url': 'https://gitlab.com/Murthy10', 'state': 'active', 'name': 'Samuel Kurath',
                    'avatar_url': 'https://gitlab.com/uploads/-/system/user/avatar/1148466/avatar.png', 'id': 1148466,
                    'username': 'Murthy10'},
         'milestone': {'iid': 1, 'due_date': '2017-09-26', 'start_date': '2017-09-18',
                       'updated_at': '2017-09-20T16:02:13.637Z', 'title': 'Project setup', 'id': 378341,
                       'project_id': 4162828,
                       'description': 'Initialize the project and setup a suitable project environment.',
                       'state': 'active', 'created_at': '2017-09-20T16:01:19.687Z'}, 'weight': None, 'upvotes': 0}]
