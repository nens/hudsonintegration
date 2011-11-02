from fabric.api import sudo
from fabric.context_managers import cd


env['hosts'] = ['buildbot.lizardsystem.nl']


def update():
    """Just a simple 'svn up' and 'bin/buildout' on the server."""
    with cd('/var/lib/jenkins/hudsonintegration'):
        sudo('svn up', user='jenkins')
        sudo('bin/buildout', user='jenkins')
