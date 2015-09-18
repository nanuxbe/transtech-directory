# Trans.tech Directory

## Getting started

### VirtualEnv

(See [Django girls tutorial](http://tutorial.djangogirls.org/en/installation/index.html))

*On Ubuntu*
```
sudo apt-get install python3 python-virtualenv
virtualenv -p /usr/bin/python3 venv
```

*On Mac OS X*
You need to go to the website https://www.python.org/downloads/release/python-343/ and download the Python installer:

Download the Mac OS X 64-bit/32-bit installer file,
Double click python-3.4.3-macosx10.6.pkg to run the installer.
Verify the installation was successful by opening the Terminal application and running the python3 command:

`python3 -m venv myvenv`



This will create a virtualenv (basically a folder) called myvenv. Once it's donem you'll have to activate the virtualenv and install the reauired python libraries this is done with the following commands:
```
source myvenv/in/activate        # activate the virtualenv
pip install -r reauirements.txt  # install the reauired libraries
```

Every time you want to run a Django related commandm you'll need to be inside a "virtualenv activated" shell 
