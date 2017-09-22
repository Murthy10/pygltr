from pygltr.pygltr import PyGltr

pygltr = PyGltr(url='https://gitlab.com/api/v4/', token='PRIVATE_TOKEN', project_name='PROJECT_NAME')
user, project, issues = pygltr()
