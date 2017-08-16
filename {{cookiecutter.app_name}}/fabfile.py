from fabric.api import *
from fabric.context_managers import prefix
from cuisine import *
from fabtools import require
import os

env.use_ssh_config=True
env.hosts = ['{{ cookiecutter.project_slug }}']
pro_name = '{{ cookiecutter.project_slug }}'
venv_path = '/home/ubuntu/.virtualenvs/{{ cookiecutter.project_slug }}'
pip_path = venv_path + '/bin/pip'
package_path = venv_path + '/lib/python3.5/site-packages/'+pro_name
python_path = venv_path + '/bin/python'


def server_check():
    run("df -h")
    run("uname -a")
    run("uptime")


def project_debug():
    with cd(pro_name):
        run("%s -V" % (python_path,))
        run("docker info")


def pack():
    local('python setup.py sdist --formats=gztar', capture=False)


def deploy():
    put("./requirements.txt", pro_name)
    put("./.tmuxp.yaml", pro_name+"/.tmuxp.yaml")
    with cd(pro_name):
        run(pip_path + " install -U -r requirements.txt")
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist
    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/tmp/%s' % filename)
    # install the package in the application's virtualenv with pip
    run(pip_path + ' install -U /tmp/%s' % filename)
    # remove the uploaded package
    run('rm -rf /tmp/%s' % filename)
    run('rm -rf /tmp/%s' % filename)
    dir_ensure(pro_name)
    put("scripts", pro_name)
    put("Dockerfile", pro_name)
    project_debug()
