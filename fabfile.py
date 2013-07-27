from fabric.api import run,env,local,settings
from fabric.operations import sudo
from fabric.context_managers import cd
import os

HOME = os.getenv("HOME")
env.user = "haradashinya"
env.hosts = ["ubuntu@54.249.237.92"]
env.key_filename = ["%s/pickalize.pem" %HOME]




def try_cmd(host_type,cmd):
    run_cmd = host_type(cmd)

def host_type():
    run("uname -s")


# push to ec2 instance.
def push():
    with settings():
        try_cmd(local,"git pull")
        try_cmd(local,'find . -name "*.pyc" -delete')
        try_cmd(local,"git push origin master")
        with cd("/var/www/static_blog"):
            try_cmd(sudo,"git pull origin master")


# push --amend



