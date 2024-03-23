#!/usr/bin/python3
# a find and replace script
import re
from fabric.api import *


file_path = "temp"
count = 0

with open(file_path, 'r') as file:
    for line in file:
        count += 1
        # match = re.search(",('\w+\s*\w*\s*\w*\s*\w*\s*\w*')\),$", line) # for amenities
        match = re.search(',(\S+)\),$', line)   # for states
        # match = re.search(",('\w+\s*\w*','\S+')\),$", line) # for cities
        print(match.group(1))
        local(f'sed -i "{count}s/,{match.group(1)})/)/g" temp') 
        local(f'sed -i "{count}s/(/({match.group(1)},/" temp')
    local(f'sed -i "{count}s/),/);/g" temp')
