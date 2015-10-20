# Grotty script to set-up the OpenPDS registry.

import pexpect

# Run OpenPDS' manage.py syncdb script.
server = pexpect.spawn('python manage.py syncdb')

server.expect('no\):\s')
server.sendline('no')
server.expect(pexpect.EOF, timeout=None)




