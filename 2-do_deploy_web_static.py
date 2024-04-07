#!/usr/bin/python3
"""
an archive to your web servers,
using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['18.234.192.206', '3.89.146.150']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name  = archive_path.split("/")[-1]
        f_name_exta = file_name .split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, f_name_exta))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name , path, f_name_exta))
        run('rm /tmp/{}'.format(file_name ))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, f_name_exta))
        run('rm -rf {}{}/web_static'.format(path, f_name_exta))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, f_name_exta))
        return True
    except:
        return False

