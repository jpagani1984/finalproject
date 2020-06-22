import os
import sys

cwd = os.getcwd()
env_dir = os.path.join(cwd, 'env')
project_dir = os.path.join(cwd, 'myproject')

# Use the python executable from inside our virtualenv
# https://help.dreamhost.com/hc/en-us/articles/215769548
INTERP = os.path.join(env_dir, 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add virtualenv packages to the start of the path
sys.path.insert(0, os.path.join(env_dir, 'bin'))
sys.path.insert(0, os.path.join(env_dir, 'lib', 'python2.7', 'site-packages'))
sys.path.insert(0, os.path.join(env_dir, 'lib', 'python2.7', 'site-packages', 'django'))

# Add brickwatch django project to the *end* of the path
# (so it will be checked last).
sys.path.append(project_dir)

# Set environment variables for django to use
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()