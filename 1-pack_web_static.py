#!/usr/bin/python3
# prepare tar file
from fabric.api import local
from time import strftime


def do_pack():
    """generate .tgz archive"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
