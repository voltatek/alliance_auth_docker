Included:
* Dockerfile
* Docker-compose

# Contents
- [Docker Stack](#Installing-Docker-Stack)
- [Updating Auth](#Updating-Auth)
- [Installing Plugins](#Installing-Plugins)


# Installation

## Image

The docker image is ready to use if you understand docker yourself and

``image: milleruk/allianceauth``

## Traefik
This Repo assumes you have Traefik installed and understand how to use it.

I have created a stack ready for production here and

https://github.com/milleruk/TraefikStack/

## Installing Docker Stack:

Clone the Repo to your own server
```
git clone https://github.com/milleruk/alliance_auth_docker.git
```

edit the ```conf/local.py``` for your eve api and mysql info and reflect the mysql info in docker-compose.yml

edit ```setup.sql``` to reflect the database settings you have added above, This is a start up script that will create the base database on MYSQL Docker startup

### Plugins
Please see here for CORE features and services

Features - https://allianceauth.readthedocs.io/en/latest/features/

Services - https://allianceauth.readthedocs.io/en/latest/installation/services/


edit ```.env``` to reflect the subdomain and domain name you are choosing for auth to be installed on

run ```docker-compose up -d``` to bring the docker stack online

run ```docker-compose logs -f --tail=20``` 

When the images have finished downloading and are running

run the following command to enter in the data to the database

```docker exec -it aa-auth python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic && /usr/bin/supervisord```

Once this has completed we are now going to create our `SuperUser`

run ```docker exec -it aa-auth python manage.py createsuperuser```

And we are done!

## Updating Auth:

Run the following commands in the following order

```docker exec -it aa-auth pip install --upgrade allianceauth```

```docker exec -it aa-auth allianceauth update /home/allianceserver/myauth```

```docker exec -it aa-auth python manage.py migrate```

```docker exec -it aa-auth python manage.py collectstatic```

```docker exec -it aa-auth supervisorctl restart myauth:```



## Installing Plugins:

To install plugins run the following commands depending on which plugin you are using

### Git
```docker exec -it aa-auth pip install git+https://github.com/##########```
Replacing # with the location of the git repo

### PIP
```docker exec -it aa-auth pip install ########```
Replacing # with the plugin pip name

Add `'PLUGIN NAME'` to INSTALLED_APPS in your `conf/local.py` settings.

Run migrations and restart your AA server

```docker exec -it aa-auth python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic && /usr/bin/supervisord```


