# pygltr
Python script to get GitLab Time Reports, it uses the GitLab API  

## Usage
If you use pygltr from the command line it will get you a CSV file with a list of all issues and some basic information.
```bash
usage: pygltr.py [-h] -t TOKEN -p PROJECT [-u URL] [-f FILE]

Get time tracking data from GitLab

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Private GitLab token
  -p PROJECT, --project PROJECT
                        Project name
  -u URL, --url URL     URL of the GitLab API
  -f FILE, --file FILE  CSV output filename

```

Beside of the usage is as a script pygltr provides the class PyGltr which is ready to use from your own code.

### Script example

```bash
python pygltr.py -t TOKEN -p PROJECT
```
Output file (default) issues.csv:

| id | issue                              | milestone      | estimate | spent | 
|----|------------------------------------|----------------|----------|-------| 
| 5  | Setup a latex template             | Project setup  | 7200     | 3600  | 
| 4  | Define milestones                  | Project setup  | 7200     | 5400  | 
| 3  | Create a physical model            |                | 0        | 0     | 
| 2  | Setup CI                           | Project setup  | 7200     | 3600  | 
| 1  | Functional tests support           |                | 0        | 0     | 


### Code example
```python
from pygltr.pygltr import PyGltr

pygltr = PyGltr(url='https://gitlab.com/api/v4/', token='PRIVATE_TOKEN', project_name='PROJECT_NAME')
user, project, issues = pygltr()
```