#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
exe: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['18.234.192.206', '3.89.146.150']


def do_pack():
    """All files in the folder web_static added to the final archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """Upload the archive to the /tmp/ directory of the web server"""
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


def deploy():
    """Call the do_pack() function and store
	the path of the created archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
