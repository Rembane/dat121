from datetime import datetime
from urllib import urlretrieve 
import os.path, subprocess

urls = ['http://www.cse.chalmers.se/~bernardy/pp/index.org',
'http://www.cse.chalmers.se/~bernardy/pp/Lectures.org',
'http://www.cse.chalmers.se/~bernardy/pp/Schedule.org',
'http://www.cse.chalmers.se/~bernardy/pp/pp.css']

for url in urls:
    urlretrieve(url, os.path.join('site', url.split('/')[-1].strip()))

subprocess.call(['git', 'add', 'site'])
subprocess.call(['git', 'commit', '-m', u'Autocommit %s' % unicode(datetime.now())])
subprocess.call(['git', 'push'])
