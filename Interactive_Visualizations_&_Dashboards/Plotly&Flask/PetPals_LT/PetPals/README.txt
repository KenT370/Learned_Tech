This is the application.  Each code or folder will either contain a README.txt file or comments
within the actual code to explain what is happening and how it fits into the overall application.

CSS: Contains the css file and images used to style the application.

Static/JS:  Contains the Javascript files that are used to compile and create the graph.

Templates:  Contains the HTML files that provide the webpage skeleton.

__init__.py: Marks the file as a Python package directory so it allows different files/programs the
  ability to import modules(programs) from this folder
  
app.py:  Contains the code necessary to run the flask application.  This is the backbone since it 
  allows the different files/databases to communicate with eachother.
  
models.py: Creates the database and the fields so that the Heroku PostGres SQL database knows what to expect
  when new data is being added to it. 
  
pets.sqlite: This was the databased used on my local machine to test my application.  
