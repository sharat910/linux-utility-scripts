import subprocess
import sys
import os

def runProcess(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

if __name__ == '__main__':
	code = sys.argv[1]
	for line in runProcess(['xinput']):
		#print line
		if 'PS/2 Generic Mouse' in line:
			_,a = line.split("=")
			num = a.split("\t")[0]
			#print num
			command = 'xinput set-prop %s \"Device Enabled\" %s'%(num,code)
			os.system(command)
			break