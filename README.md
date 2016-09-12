# learning_journal
##Code Fellows Python 401 Learning Journal Project

This project covers the setup and deployment of a learning journal using Pyramid, a python web framework.  The visual look of the page will be sleek and clean (which it's not really yet, but I'll keep working on it).  The back-end guts of the project will be updated in an iterative manner over the coming days and eventually new learning journal entries will be entered here, live on a deployed Heroku dyno.


##Heroku Deployment

This project will be deployed to Heroku periodicially throughout it's devleopment, you can take a look at it here:

https://derekcf401learningjournal.herokuapp.com/

###Cited Sources
  -https://codefellows.github.io/sea-python-401d4/assignments/pyramid_lj_1.html
  -https://codefellows.github.io/sea-python-401d4/lectures/pyramid_heroku.html
  -(many other class repo resources)
  -Big thanks to Will, Cris and Nick for their assistance getting this up and running.

## Day 1

Today we initally installed Pyramid into our repo and wired up basic views using explicit functions.

## Day 2
For day two's assignment I completely refactored the views with decorators and swapped out the old html for fancy jinja2 templates.  Thanks/credit to Mike for helping me set up the detail view with the regular expressions.

### Cited Sources:
  - General Help: http://pythoncentral.io/sqlalchemy-faqs/

## Day 3

On day three we reinstalled Pyramid using the SQLAlchemy package and refactored all our data sources to pull from a local sqlite db.

### Cited Sources:
 - Help with date formatting: http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
 - Jinja 2 date formatting: http://stackoverflow.com/questions/4830535/python-how-do-i-format-a-date-in-jinja2
 - Reset style sheet from: http://meyerweb.com/eric/tools/css/reset/

# Day 4

On day 4 we switched to a PostgreSQL db and deployed to Heroku, rewiring as necessary to hook up to PostgreSQL instead of SQLite.

# Day 5

On Day 5 we implemented a log in prompt and secured some of our views so that only authorized users can add and edit posts.

