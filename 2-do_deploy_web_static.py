#!/usr/bin/python3
"""This Fabric script distributes an archive to my web servers
"""
from datetime import datetime
from os.path import exists
from fabric.api import local, env, put, run

# set the server hosts for web-01 and web-02
env.hosts = [
    "52.87.254.150",
    "52.86.39.247",
]
# set the username
env.user = "ubuntu"

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct path where archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(now)

    # use fabric function to create directory if it doesn't exist
    local("mkdir -p versions")

    # Use tar command to create a compresses archive
    archived = local("tar -cvzf {} web_static".format(archive_path))

    # Check archive Creation Status
    if archived.return_code != 0:
        return None

    return archive_path

def do_deploy(archive_path):
    """Distributes an archive to my web servers

    Args:
        archive_path (str): The path to my archive

    Returns:
        bool: true if archive path exists or false if otherwise
    """
    if exists(archive_path):
        # extract the archive filename
        archive_filename = archive_path.split("/")[1]
        # create the remote path
        rem_path = "/tmp/{}".format(archive_filename)
        # upload the archive file to /tmp/
        put(archive_path, rem_path)
        # extract filename without extension
        archive_name = archive_filename.split(".")[0]
        # remote directory path
        rem_dir_path = "/data/web_static/releases/{}/".format(archive_name)
        # create the directory to contain the uncompressed archive file
        run("mkdir -p {}".format(rem_dir_path))
        # uncompress archive
        run("tar -xzf {} -C {}".format(rem_path, rem_dir_path))
        # delete the archive from the server
        run("rm {}".format(rem_path))
        run("mv -f {pth}web_static/* {pth}".format(pth=rem_dir_path))
        run("rm -rf {}web_static".format(rem_dir_path))
        # delete the existing symbolic link
        sym_link = "/data/web_static/current"
        run("rm -rf {}".format(sym_link))
        # create a new symbolic link
        run("ln -s {} {}".format(rem_dir_path, sym_link))
        return True
    return False
    
    
