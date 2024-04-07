#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo
using the function do_pack
"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """web_static must be added to the final archive"""
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        archived_file_name = f'web_static_{current_time}.tgz web_static'
        local("mkdir -p versions")
        local(f"tar -cvzf versions/{archived_file_name}")
        return "versions/"
    except Exception as err:
        return None
