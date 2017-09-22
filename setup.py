from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='pygltr',
    version='0.8.0',
    description='Python script to get GitLab Time Reports',
    long_description=readme,
    author='Samuel Kurath',
    author_email='samuel.kurath@gmail.com',
    url='https://github.com/murthy10/pygltr',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs'))
)