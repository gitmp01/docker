#!/usr/bin/env python3

import subprocess

out = subprocess.run("./bin/nice")

if out.returncode == 0:
    print('Cool!')
else:
    print('Uhm...')