# AttendanceManager
The aim of this project is to provide a centralized online 
resource for members of the CU Climbing Team to keep track 
of their attendance, competition, and fundraising requirements. 
Users of this system will swipe their student IDs in a card reader 
to register their attendance through a http request to a Django-based 
REST API. Users may log in to their accounts via the provided Django
web app to manage their accounts, view their team records, and receive
important information posted by the team captains. Admin users can create
user records and post announcements on the team's homepage. 

#### Built With
* [Django](https://www.djangoproject.com/) - A high-level python web framework.
* [Django Rest Framework](https://www.django-rest-framework.org/) - A third-party Django toolkit for building REST APIs.
* [PostgreSQL](https://www.postgresql.org/) - An open-source relational database management system.
* [Bootstrap](https://getbootstrap.com/) - An open-source CSS framework. 
* [RaspberryPi](https://www.raspberrypi.org/) - A single-board computer running Linux, used for modular embedded systems projects.

#### Hosted Using
* [Amazon Web Services EC2](https://aws.amazon.com/ec2/) - A web service providing secure, scalable cloud computing.
* [Gunicorn](https://gunicorn.org/) - A python wsgi HTTP server.
* [Nginx](https://www.nginx.com/) - A reverse proxy server. 

#### Hardware Used
* [Raspberry Pi Zero W](https://www.sparkfun.com/products/14277) - Raspberry Pi's smallest model with full wifi and bluetooth functionality.
* [Basic 16x2 LCD Screen](https://www.sparkfun.com/products/255) - A simple text screen to display usage prompts and information.
* [MagTek MSR100 Card Reader](https://www.amazon.com/POSUNITECH-Magnetic-Collector-MSR100-information/dp/B06XSHLYC2/ref=sr_1_fkmr0_2?keywords=MagTek+MSR100&qid=1566332460&s=gateway&sr=8-2-fkmr0) - A magnetic card reader.


## Embedded Systems Setup 
TODO

## Deployment to Ubuntu EC2 Instance
Create an Ubuntu EC2 instance in the [EC2 Console](https://aws.amazon.com/console/),  adding a security rule enabling access to SSH and HTTP ports from all hosts.
Then log into the instance as user ubuntu. For more info about logging into an EC2 instance, click the "connect" tab in the console and follow the instructions.

    $ ssh -i PrivateKeyFile.pem ubuntu@ec2-xx-xxx-xxx-xxx.us-east-2.compute.amazonaws.com
Switch to root user, create new Linux user and give superuser permissions. Additionally allow new user to login via ssh. 

    $ sudo -s 
    # adduser cuclimbingteam
    # usermod -aG sudo cuclimbingteam
    # rsync --archive --chown=cuclimbingteam:cuclimbingteam ~/.ssh /home/cuclimbingteam
Then disconnect from the EC2 instance and log back in as the new user.

    $ ssh -i PrivateKeyFile.pem cuclimbingteam@ec2-xx-xxx-xxx-xxx.us-east-2.compute.amazonaws.com
Setup ufw (uncomplicated firewall) to allow communications on SSH port, but no other port. First list all apps to confirm OpenSSH is an option.

    $ sudo ufw app list
    Available applications:
        OpenSSH
        ...
Set ufw rules to allow OpenSSH. This is very important to do before enabling the firewall, otherwise you will lock yourself out of the EC2 instance!

    $ sudo ufw allow OpenSSH
    $ sudo ufw enable
    $ sudo ufw status
    To              Action  From
    --              ------  ----
    OpenSSH         Allow   Anywhere
    OpenSSH (v6)    Allow   Anywhere
Now the EC2 instance is configured for general use and ready to start settingup the webapp. We will start by installing the project dependencies.

    $ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
Clone the source code from this repository and step into the new directory.
    
    $ git clone https://github.com/hainsworth99/AttendanceManager
    $ cd AttendanceManager
Install virtualenv and start a new development environment, which we will name `attendancemanagerenv`.
    
    $ sudo -H pip3 install --upgrade pip
    $ sudo -H pip3 intall virtualenv
    $ virtualenv attendancemanagerenv
Activate the environment and install the necessary python packages for the project.

    $ source attendancemanagerenv/bin/activate
    (attendancemanagerenv) $ pip install django djangorestframework django-rest-auth psycopg2 gunicorn
We have now installed all the necessary source code, dependencies, and packages required to run the project. We may now begin to configure the django application itself, starting off by setting up a postgresql database. First log into the psql terminal as user `postgres`.

    (attendancemanagerenv) $ sudo -u postgres psql 
Then create the database and user roles for the project.

    postgres=# CREATE DATABASE attendancemanagerdb;
    postgres=# CREATE USER attendancemanageruser WITH PASSWORD 'xxxx';
    postgres=# ALTER ROLE attendancemanageruser SET client_encoding TO 'utf8';
    postgres=# ALTER ROLE attendancemanageruser SET default_transaction_isolation TO 'read committed';
    postgres=# ALTER ROLE attendancemanageruser SET timezone TO 'MST';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE attendancemanagerdb TO attendancemanageruser;
    postgres=# \q
Now that our database is configured, we can load the database login information to the project settings. Although the below example shows placing the login info directly into the settings file, this is not advisable. For security reasons, store sensitive information such as passwords and secret keys in environment variables or a configuration file.  
    
In ~/AttendanceManager/AttendanceManager/settings.py:
    
    ...
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': attendancemanagerdb,
            'USER': attendancemanageruser,
            'PASSWORD': 'xxxx',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ...
    
Also in `settings.py`, configure the following values for production.
    
    ... 
    DEBUG = False
    ALLOWED_HOSTS = [ 'server_domain_name', 'server_ip']
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    ... 
Migrate the project models to the database, create a superuser for the account, and load the static files for the project.

    (attendancemanagerenv) $ ./manage.py makemigrations
    (attendancemanagerenv) $ ./manage.py migrate
    (attendancemanagerenv) $ ./manage.py createsuperuser
    (attendancemanagerenv) $ ./manage.py collectstatic
The django application should be ready to run at this point. You can test by running django's development server on port 8000. You will need to allow port access for port 8000 through both ufw and the instance's security group.

    (attendancemanagerenv) $ sudo ufw allow 8000
    (attendancemanagerenv) $ ./manage.py runserver 0.0.0.0:8000

Verify that the application is working at [http://project_ip_or_domain:8000](). Resolve any errors that you encounter before moving on. Now test gunicorn's ability to serve the project. Run the following command and visit the same link to verify this functionality. 

    (attendancemanagerenv) $ gunicorn --bind 0.0.0.0:8000 AttendanceManager.wsgi
We can now exit the virtualenv. Also delete the ufw rule allowing port 8000, since we only needed that for testing purposes.

    (attendancemanagerenv) $ deactivate
    $ sudo ufw delete allow 8000
Next we will create service and socket files for gunicorn to serve the application.

In /etc/systemd/system/gunicorn.socket:
    
    [Unit]
    Description=gunicorn socket
    
    [Socket]
    ListenStream=/run/gunicorn.sock
    
    [Install]
    WantedBy=sockets.target
    
In /etc/systemd/system/gunicorn.service:
    
    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target
    
    [Service]
    User=cuclimbingteam
    Group=www-data
    WorkingDirectory=/home/cuclimbingteam/AttendanceManager
    ExecStart=/home/cuclimbingteam/AttendanceManager/attendancemanagerenv/bin/gunicorn \
        --access-logfile - \
        --workers 3 \
        --bind unix:/run/gunicorn.sock \
        AttendanceManager.wsgi:application
    
    [Install]
    WantedBy=multi-user.target
Start and enable the socket. Then test that the socket can receive requests using curl. During this test, curl should print out some html, the response to the http request. 

    $ sudo systemctl start gunicorn.socket
    $ sudo systemctl enable gunicorn.socket 
    $ curl --unix-socket /run/gunicorn.sock localhost
Additionally, verify that gunicorn is running with the following command.
    
    $ sudo systemctl status gunicorn
Finally, we will setup nginx to proxy pass to gunicorn via the socket we just created.

In /etc/nginx/sites-available/AttendanceManager:

    server {
        listen 80;
        server_name server_ip domain.com www.domain.com;
    
        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /home/cuclimbingteam/AttendanceManager;
        }
    
        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
        }
    }
Make sure to replace the values in `server_name` with the ip and domain values of your server. Now link the `sites-available` to `sites-enabled`, test, and start nginx. 

    $ sudo ln -s /etc/nginx/sites-available/AttendanceManager /etc/nginx/sites-enabled
    $ sudo nginx -t 
    $ sudo systemctl restart nginx
    $ sudo ufw allow 'Nginx Full'
The application should be up and running on the ip address or domain name associated with the server. Test it out by visiting the ip or domain in a web browser.

## Authors
* __Harold Ainsworth__ - _initial work_

## Acknowledgements
* [Initial Server Setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) - by Justin Ellingwood
* [How to Setup Django with Postgres, Nginx, and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) - by Justin Ellingwood
* [Django for APIs](https://djangoforapis.com/) - by William S. Vincent
