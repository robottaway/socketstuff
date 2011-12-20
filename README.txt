socketstuff README

This is a testbed project to try out a few asynchronous io concepts in python
using gevent and greenlets


Getting dev going...
----------------------

NOTE: info on env OS X/Windows/Linux below!

Do the following in your virtualenv:

python setup.py develop

That'll get you where you can develop on this while using it.

You'll need to use pip to install the requirements, note that for gevent you'll
need libevent 2 installed and the header files in a location that is findable.

When ready to install this apps dependencies do:

pip install -r requirements.txt

It'll take a bit to install but once it's going you should be able to:

sudo socket-serve-reload development.ini

Note the 'sudo' above is needed for the Flash server to work and so we can use
Flash sockets with socket io.


On Mac OS X (tested on Snow Leopard)
-------------------------------------

Use Mac Ports to install libevent:

sudo port install libevent

Then you'll want to run the following:

export CFLAGS=-I/opt/local/include

Which'll let gevent point to the header files when building.

User Mac Ports to install redis:

sudo port install redis


On Windows
-----------

TODO


On Linux
---------

TODO
