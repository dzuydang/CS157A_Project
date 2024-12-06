Project Members: 
Fabian Garcia Quinonez
Javier Aguilar Ochoa
Dzuy Dang
Saul Figueroa
Travis Nguyen

Steps to run program:
1. Install the following:
   - Python
   - Django (pip install django)
   - mysqlclient (pip install mysqlclient)
   - MySQLWorkbench
   - Django CORS Headers (pip install django-cors-headers)
   - Live Server (VSCode Extension)
   - VSCode

2. To create the databases, go into the MySQLWorkbench. Create 2 new files. One will be for creating the tables and the other will be for populating the tables.
     a. Use the db.sql file (in CS157A_Project/cs157a/evidenceManager) which contains the schemas for the tables needed. Then, run that to create the tables.
     b. Next, use the tableInfo.sql (same directory) and populate the tables. Verify that the tables have been populated and created before moving on.

3. Next, using your created database name, and the sql username and password local to your machine, go into settings.py (in CS157A_Project/cs157a/evidenceManager/evidenceManager) and go to the "DATABASES" section. Change the NAME, USER, and PASSWORD sections to the appropriate credentials for your machine. HOST and PORT may need to be changed, based on  how your machine is configured.

4. Apply database migrations by running 'python manage.py migrate'.
5. Start the Django development server by navigating to the evidenceManager directory and running 'python manage.py runserver'. This will start up the Django backend server to handle our frontend API requests.
6. Navigate to the frontend folder in VSCode and right click while having searchPage.html open. Click on "Open with Live Server", which will open the live server to display the front end.
7. Now queries can be set up and run as needed!

DIVISION OF LABOR:
   - Dzuy Dang: Frontend, Backend, Frontend-Backend Connectivity, Readme file
   - Saul Figueroa: ER Diagram, Report, Presentation Slides
   - Travis Nguyen: Database setup, Database population, Settings.py setup
   - Javier Aguilar Ochoa: Report, Presentation Slides
   - Fabian Garcia Quinonez: 
