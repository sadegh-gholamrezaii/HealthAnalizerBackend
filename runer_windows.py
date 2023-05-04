import subprocess
from health_analyzer.health_analyzer import settings
 
'''
Hello
To start the database of this project, you can proceed as follows:
1. First install PostgreSQL    (https://www.postgresql.org/download/)

2. Open CMD and enter the following command:
       psql -U postgres
and Enter the master password, 
If the psql command is not recognized, check the environment variable.

3. Then create a user in it:
        postgres=#  CREATE USER username WITH PASSWORD 'password';
        
4. Create a database:
        postgres=#  CREATE DATABASE database_name;

5. And finally, give the ownership of that database to the user:
        postgres=#  ALTER DATABASE database_name OWNER TO username;

You can make sure you did it right with the following command:
        postgres=#  \l

Then Enter the values in settings.DATABASES .
'''

settings.DATABASES ={
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '127.0.0.1',
    'PORT': '5432',
      }
} 
 
process = None
project_path = "C:\\Users\\sad\\Desktop\\AZnarm\\HealthAnalizerBackend"


# list of commands
commands = [
    project_path+'\\main_set\\Scripts\\activate',
    f'pip install -r {project_path}\\requirements.txt',
    f'{project_path}\\main_set\\Scripts\\python.exe {project_path}\\health_analyzer\\manage.py makemigrations',
    f'{project_path}\\main_set\\Scripts\\python.exe {project_path}\\health_analyzer\\manage.py migrate',
    f'{project_path}\\main_set\\Scripts\\python.exe {project_path}\\health_analyzer\\manage.py runserver',
    
]

# exe
for cmd in commands:
    process = subprocess.Popen(cmd, shell=True)

#process.send_signal(subprocess.signal.CTRL_C_EVENT)    #stop with ctrl+c
