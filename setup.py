import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid', 'pyramid_debugtoolbar']

setup(name='socketstuff',
      version='0.0',
      description='socketstuff',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="socketstuff",
      entry_points = """\
[paste.server_factory]
sioserver = pyramid_socketio.pasteserve:server_factory
sioserver_patched = pyramid_socketio.pasteserve:server_factory_patched

[console_scripts]
socketio-serve-reload = pyramid_socketio.servereload:socketio_serve_reload
socketio-serve = pyramid_socketio.serve:socketio_serve
""",
      paster_plugins=['pyramid'],
      )

