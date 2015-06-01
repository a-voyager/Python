#!usr'+os.sep+'bin'+os.sep+'python
#Filename:backup.py
import os
import time
print 'begin backuping...'
input = raw_input('please input the source dir>>')
source = [''+os.sep+'home'+os.sep+''+os.uname()[1]+''+os.sep+'']
if not len(input)==0:
    source[0]=input
destination = ''+os.sep+'home'+os.sep+''+os.uname()[1]+''+os.sep+'backup'
print 'are you sure to backup these dir:(y'+os.sep+'n)'
for i in source:
    print i
tmp=raw_input('>>')
if (tmp != 'y' ) & (tmp != 'Y'):
    print 'stopped'
    exit()
if not os.path.exists(destination):
    os.mkdir(destination)
day = destination+os.sep+time.strftime('%Y%m%d')
now = day + os.sep + time.strftime('%H%M%S')+'.zip'
if not os.path.exists(day):
    os.mkdir(day)
    print 'dir created succeed!begining...'
command = 'zip -qrv %s %s'%(now, ' '.join(source))
if os.system(command)==0:
    print 'backup succeed!'
else:
    print 'sorry,backup faild!'