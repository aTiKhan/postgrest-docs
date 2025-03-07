#!/usr/bin/env python
from livereload import Server, shell
from subprocess import call
## Build docs at startup
call(['sphinx-build', '-b', 'html', '-a', '-n', 'docs', '_build'])
server = Server()
server.watch('docs/**/*.rst', shell('sphinx-build -b html -a -n docs _build'))
# For custom port and host
# server.serve(root='_build/', host='192.168.1.2')
server.serve(root='_build/')
