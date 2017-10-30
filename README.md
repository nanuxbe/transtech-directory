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

### Getting your environment ready

In the main project directory, you'll find a file called `environ.py.dist`. Make a copy into a file named `environ.py` and edit to fit the settings on your computer. If you are just curious to get the project started, you can just copy the file and start the server

### Compiling SaSS into CSS

This project is configured to use [Ruby Compass](https://rubygems.org/gems/compass/versions/1.0.3) to build CSS.

*On Ubuntu*

`sudo apt-get install ruby-compass`

*On Mac OS X*

`sudo gem install compass`

*On Windows*

In a terminal:
`gem install compass`


Once Compass is installed, from the main project directory, run:

- `compass compile` to compile SaSS source once
- `compass watch` to have compass watch for changes and recompile SaSS files after each change


### Starting the server

- Make sure you are in a virtualenv-activated shell
- boostrap the database: `./manage.py migrate`
- create a user for yourself: `./manage.py createsuperuser`
- start the actual server: `./manage.py runserver`
