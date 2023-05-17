import subprocess

'''
Hello
A)  To start the virtual environment ,
    After cloning the repository,
    enter the "HealthAnalizerBackend" folder,
    open CMD and enter the following commands:
1.      pip install virtualenv
2.      virtualenv name_of_env

Then set the values  <-- :
'''

project_path = r"C:\Users\sad\Desktop\az_narm\HealthAnalizerBackend"  # <--    change it

name_of_env = "name_of_env"  # <-- change it

Scripts_Path = f"{project_path}\\{name_of_env}\\Scripts"


'''
B)  To start the database of this project, you can proceed as follows:
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

Then go to:
        health_analyzer > health_analyzer > settings.py
and set the DATABASES values :  (<--)
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': '',     # <--
                'USER': '',     # <--
                'PASSWORD': '', # <--
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }   
        }
           
'''

process = None

# list of commands
commands = [
    f'{Scripts_Path}\\pip install -r {project_path}\\requirements.txt',
    f'{Scripts_Path}\\python.exe {project_path}\\health_analyzer\\manage.py makemigrations',
    f'{Scripts_Path}\\python.exe {project_path}\\health_analyzer\\manage.py migrate',
    f'{Scripts_Path}\\python.exe {project_path}\\health_analyzer\\manage.py runserver',
    
]

# exe
for cmd in commands:
    process = subprocess.run(cmd, shell=True)

#process.send_signal(subprocess.signal.CTRL_C_EVENT)    #stop with ctrl+c
