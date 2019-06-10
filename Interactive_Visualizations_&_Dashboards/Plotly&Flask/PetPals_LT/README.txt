The Goal of this application is to take user inputted data, store it in a database, retrieve it, and present it back to the user in the form of a visual.

This is a Heroku hosted application.  Visit https://petslocate.herokuapp.com/ to view the completed app.

The folder PetPals contains the code for the full-stack application. 
The other files are necessary for deployment to Heroku and are explained below:

Procfile:  Utilizes Gunicorn to start the application
initdb.py:  Creates the first instance of the database
requirements.txt:  Notifies Heroku on the packages that need to be installed in order for the application to run.
run.sh:  Run's the flask application.

