#!/usr/lib/python
import yaml
import socket
import subprocess
import os
from git import Repo

def git_pull(PATH_OF_GIT_REPO):
    repo = Repo(PATH_OF_GIT_REPO)
    origin = repo.remote(name='origin')
    origin.pull()
    
def git_update(PATH_OF_GIT_REPO):
    repo = Repo(PATH_OF_GIT_REPO)
    origin = repo.remote(name='origin')
    repo.git.add(update=True)
    repo.index.commit(COMMIT_MESSAGE)    
    origin.push()
    
def get_ip_address() -> str:

    try:
        _arg = "ip route list"
        _p = subprocess.Popen(_arg, shell=True, stdout=subprocess.PIPE)

        _data = _p.communicate()
        _temp_str = str(_data[0]).split()
        _ip_address = _temp_str[_temp_str.index("src") + 1]

    except:
        _ip_address = ""

    return _ip_address

if __name__ == "__main__":
    PATH_OF_GIT_REPO = r'/home/pi/MBLUE-config/.git'  # make sure .git folder is properly configured
    git_pull(PATH_OF_GIT_REPO)

    with open("/home/pi/MBLUE-config/config.yaml", "r") as file:
        ip_addresses = yaml.safe_load(file)

    print("Existing IP addresses: ", ip_addresses)

    hostname = socket.gethostname()
    ip_address = get_ip_address()

    if ip_addresses and ip_address != "":
        if "right" in hostname.lower():
            ip_addresses["RPI_KNEE_RIGHT_IP"] = ip_address
        elif "left" in hostname.lower():
            ip_addresses["RPI_KNEE_LEFT_IP"] = ip_address
        elif "avani" in hostname.lower():
            ip_addresses["RPI_SYNC_IP"] = ip_address

    with open("/home/pi/MBLUE-config/config.yaml", "w") as file:
        yaml.dump(ip_addresses, file)

    print("Updated IP addresses: ", ip_addresses)
    COMMIT_MESSAGE = 'commit from gitpy'
    git_update(PATH_OF_GIT_REPO)