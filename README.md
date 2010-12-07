# Preview - a Django project for previewing designs

## Requirements

You will need the following installed:

* pip
* virtualenv

## Installation

Set up a folder and virtual env:
    cd /path/to/your/workspace
	mkdir preview
	cd preview
	mkvirtualenv --no-site-packages preview
	
Install all dependencies
    pip install -r requirements.txt
Note that the MySQL-python package has a dependency on libmysqlclient-dev which needs to be installed using apt-get.  You can 
view the installed packages in your virtual env using
    yolk -l

Create a local_settings.py file which contains your database credentials.  This file is on the .gitignore list
and so needs creating manually

Load the test data using:
    ./manage.py loaddata main/fixtures/test_data.json
Note that there is a set of fixture images in assets/design-fixtures/ that go with the fixture data.

There is a single user with username "admin" and password "testing" in the fixture data.

## Testing

Run the tests with:
    ./manage.py test main
