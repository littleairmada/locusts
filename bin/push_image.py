#! /usr/bin/env python3

import os
import sys

commit_message = ' '.join(sys.argv[1:])
if not commit_message:
    print('No Commit message specified')
    sys.exit(1)

commit_cmd = [
    'docker', 'commit',
    '-m', '"{}"'.format(commit_message),
    '-a', '"littleairmada"',
    'littleairmada/locusts', 'littleairmada/locusts:latest'
]

print('COMMITTING IMAGE')
os.system(' '.join(commit_cmd))

cmd = ['docker', 'push', 'littleairmada/locusts:latest']

print('PUSHING IMAGE')
os.system(' '.join(cmd))
print('IMAGE PUSHED')
