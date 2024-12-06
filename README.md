# Caser
### Project Members
- Fabian Garcia Quinonez
- Javier Aguilar Ochoa
- Dzuy Dang
- Saul Figueroa
- Travis Nguyen

### Steps to run the program
1. Install the following
   - Python
   - Django (pip install Django)
   - mysqlclient (pip install mysqlclient)
   - MySQLWorkbench
   - Django CORS Headers (pip install django-cors-headers)
   - Live Server (VSCode Extension)
   - VSCode

2. Creating and Populating the Database
   -  To create the databases, go into MySQLWorkbench and create 2 new files. (One will be for creating the tables and the other will be for populating the tables)
   -  Find the db.sql file (in CS157A_Project/cs157a/evidenceManager) which contains the schemas for the tables needed. Then, run that to create the tables.
   -  Use the tableInfo.sql (same directory) and run it to populate the tables. Verify that the tables have been populated and created before moving on.

3. Configuring Database Connection
   -  Using your created database name, and the sql username and password local to your machine, go into settings.py (in CS157A_Project/cs157a/evidenceManager/evidenceManager) and go to the "DATABASES" section.
   -  Change the NAME, USER, and PASSWORD sections to the appropriate credentials for your machine. HOST and PORT may need to be changed, based on  how your machine is configured.

4. Apply Database Migrations
   - Apply database migrations by running 'python manage.py migrate'.
   - In the case that the migration fails, run the following:
   - '''python manage.py showmigrations'''
   - '''python manage.py migrate evidence --fake'''
   - Then retry the 'python manage.py migrate' command.
   - ![image](https://github.com/user-attachments/assets/8514875b-e9e3-494a-bc91-4001d5437002)

5. Starting Django Development Server
   - Start the Django development server by navigating to the evidenceManager directory and running 'python manage.py runserver'. This will start up the Django backend server to handle our frontend API requests.
6. Open Frontend with Live Server
   - Navigate to the frontend folder in VSCode and right-click while having searchPage.html open. Click on "Open with Live Server", which will open the live server to display the front end.
7. Running Queries
    - Now queries can be set up and run as needed!

### DIVISION OF LABOR:
   - Dzuy Dang: Frontend, Backend, Frontend-Backend Connectivity, Readme file
   - Saul Figueroa: ER Diagram, Report, Presentation Slides, Schema Refinement/Normalization
   - Travis Nguyen: Database setup, Database population, Settings.py setup, Schema Refinement/Normalization
   - Javier Aguilar Ochoa: Report, Presentation Slides
   - Fabian Garcia Quinonez: Initial Django Project Setup, Report
