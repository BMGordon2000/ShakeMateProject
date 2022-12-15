# CSC 450 - Team Project

## Team Members

- Project Manager - Bryson Harllee
- Lead Developer - Andrew Bracero
- Developer - Drake Kvaall
- Developer - Ben Gordon
- Developer - Trafton Reynolds

---

## Setting up python in Visual Studio Code

1. Make sure python has been installed on your machine. Go to [python.org](https://www.python.org/) and download the latest version of python.
2. Once installed, in the VS code terminal, enter: `pip3 install virtualenv`
3. Next, enter: `source env/bin/activate`

---

## Setting up flask in Visual Studio Code
1. Set up the FLASK_APP environment variable. In the Terminal:
   - On Windows: `set FLASK_APP=main.py`
   - On Mac/Linux: `export FLASK_APP=main.py`
2. With the virtualenv activated, run `pip install -r requirements.txt`
    - This will install ALL of the libraries in the requirements.txt file.
    - If you need to add a new library later, do `pip install ...` like normal, then do `pip freeze > requirements.txt` to update the library dependencies.
2. Run `flask db upgrade`
    - this will create a database file in `instance/test.db`. You can open this file with a SQLite Browser and look at the tables.
    - If you update a database model (e.g., DatabaseComponent.User), you must run `flask db stamp head` then `flask db upgrade` and `flask db migrate` in the Terminal for the changes to show in the database file.
3. Run `flask run` in the Terminal. You will see a URL that you can browse to show the app.

## Using pytest

1.  `pip install -U pytest`
    - This install py test in your 
2.  `py -m pytest -v`
    - using this command will run every test that has test_ or _test
    
## Website url
   - https://shakemate1.herokuapp.com/
