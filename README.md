# Preview - a Django project for previewing designs

## Requirements

You will need the following installed:
 pip
 virtualenv

## Installation

Set up a folder and virtual env:
    cd /path/to/your/workspace
	mkdir preview
	cd preview
	mkvirtualenv --no-site-packages preview
	
Install all dependencies
    pip install -r requirements.txt

Create a local_settings.py file which contains your database credentials.  This file is on the .gitignore list
and so needs creating manually

Load the test data using:
    ./manage.py loaddata main/fixtures/test_auth.json
    ./manage.py loaddata main/fixtures/test_main.json
Note that there is a set of fixture images in assets/design-fixtures/ that go with the fixture data.

There is a single user with username "admin" and password "testing" in the fixture data.

