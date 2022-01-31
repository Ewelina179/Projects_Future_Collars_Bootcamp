There are few projects created during Future Collars bootcamp.

# 1. File manager

Program modifies files and displays the contents of the file in the terminal, saves in the specified location.

<h7> How to use: </h7>
<h10> python reader.py < file path> < new location > < change1 > < optionally another change > </h10> <br> <br>
<h10>  change means: "X,Y,value" where X is row to modify (counted from 0), Y is column to modify (counted from 0) and value is targed value modified in X,Y position <h10>


# 2. Flask App with ORM

Application to manage warehouse and account.
  
  <h7> How tu use: </h7>
  
  - git clone
  - cd flask_app_with_orm
  - pip install -r requirements.txt
  - cd my_app
  - flask db init
  - flask db migrate
  - flask db upgrade
  - set FLASK_APP=app.py
  - flask run

<h7> Technological stack: </h7>
- Flask with WTForm to validate forms
- sqlite
- SQLAlchemy

# Weather

Program to check if it will be rain.

<h7> How to use: </h7>
<h10> python weather.py < API KEY from rapidapi.com > < optionally date, current date by default >
