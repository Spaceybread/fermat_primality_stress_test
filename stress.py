import os
import sys
import subprocess

i = 0

print('Monitor CPU performance to avoid damage to your hardware')
n = int(input('Instance count:  '))

procs = []
for i in range(n):
    proc = subprocess.Popen([sys.executable, 'mprime.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)

for proc in procs:
    proc.wait()
