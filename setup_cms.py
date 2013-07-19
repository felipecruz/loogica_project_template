#!/usr/local/env python
import os
import sys

from fabric.operations import local
from fabric.context_managers import lcd

TEMPLATE_URL = 'https://github.com/felipecruz/loogica_project_template/archive/master.zip'
DJANGO_CMD = 'django-admin.py startproject --template={template} {project}'

if __name__ == "__main__":
    project_name = sys.argv[1]
    with lcd(sys.argv[2]):
        local(DJANGO_CMD.format(project=project_name,
                                template=TEMPLATE_URL))
        with lcd(project_name):
            local('make dbinitial')
            local('make runserver')