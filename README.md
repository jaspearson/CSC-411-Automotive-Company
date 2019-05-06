# CSC-411-Automotive-Company
Web application for University of Southern Mississippi CSC 411 Databases project.

Youtube video walk-through:

# Step 1
## Required installs
The following packages are required installs to run this application. 
* Python 3.7.
* Django 2.1.7
* Pycharm 2018.3.4 (This is the IDE I used to build the application, but any IDE for python should work.)
* mysql-python-connector 8.0.12 

# Step 2
## Project Structure
* SQL Queries - in this folder you will find all the SQL queries needed to create the database and populate it with a seeded dataset.
* Design Materials - This folder contains the project assignment PDF, the ER Diagram and relational schema.  
* manage.py - run this file through the IDE. 

# Step 3 
## Give my app access to the database. 
* In the /CSC_411_Automotive_Company/CSC_411_Automotive_Company locate and open the secret_settings.py file. 
* Update the user and password information to match a user in your SQL database.

# Step 4 
* Navigate to {your IP address}:{Port Number}/auto_admin/. Example: 127.0.0.1:8000/auto_admin/
* The Queries for the reports are implemented as database views and available through the application Reports tab.
