

import sys
import regex
import re
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict
from errors import InvalidFormatFile


def should_install_requirement(requirement):
    should_install = False
    try:
        pkg_resources.require(requirement)
    except (DistributionNotFound, VersionConflict):
        should_install = True
    return should_install


def install_packages(requirement_list):
    try:
        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        if len(requirements) > 0:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
        else:
            print("Requirements already satisfied.")

    except Exception as e:
        print(e)

def get_exantension(file):

    step = file.split('.')
    if len(step) < 2:
        return None

    return '.'.join(step[1:len(step)])



