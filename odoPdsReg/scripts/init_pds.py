# Grotty script to set-up OpenPDS.

import os
import pexpect

# Run OpenPDS' start.py script
server = pexpect.spawn('python start.py')

server.expect('\):\s')
server.sendline('') # OpenPDS is in the default directory.
server.expect('\):\s')
server.sendline(os.environ['HOSTADDR']+':8000') 
server.expect('[1]\):\s')
server.sendline('1') # MongoDB as the back-end.
# <Sigh> MongoDB is web-scale: https://www.youtube.com/watch?v=b2F-DItXtZs
server.expect(pexpect.EOF, timeout=None)

# Run OpenPDS' manage.py syncdb script.
server = pexpect.spawn('python manage.py syncdb')

server.expect('no\):\s')
server.sendline('no')
server.expect(pexpect.EOF, timeout=None)




