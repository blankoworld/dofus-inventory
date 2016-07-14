# Dofus Inventory

**Dofus Inventory** or **Dofus map** is an application that helps users to create a database of ressources (in Dofus). Then it gives an access to an API to share data in JSON.

You can so link other application (mobile, desktop, web) to use this API and display data as you want.

[![Python 3.4](https://img.shields.io/badge/python-3.4-green.svg)](http://python.org/)
[![Django 1.9](https://img.shields.io/badge/django-1.9-green.svg)](http://djangoproject.com/)
[![CeCILL 2.1](https://img.shields.io/badge/License-CeCILL-blue.svg)](http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html)

# License

**Dofus Inventory** is licensed under the [CeCILL 2.1](http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html) license.

# Virtualenv

## Requirements on Ubuntu 14.04

  * python3
  * python3-dev
  * python-virtualenv
  * python3-pip

## Initialisation

``` bash
pip install -r requirements.txt
cd dmap
python manage.py migrate
python manage.py loaddata ressources_and_categories origines_and_espaces
```

## Create a super user to access database

```bash
python manage.py createsuperuser
```

## Launch it

```bash
python manage.py runserver
```

# Docker

## Built it

```bash
cd ..
docker build -t dmap:1.0 .
```

## Prepare database and content

```bash
mkdir /dmap_data
docker run -it --rm -v /dmap_data:/opt/database dmap:1.0 python3 manage.py migrate
docker run -it --rm -v /dmap_data:/opt/database dmap:1.0 python3 manage.py loaddata ressources_and_categories origines_and_espaces
```

# Launch it!

```bash
docker run -it --rm -p 8000:8000 -v /dmap_data:/opt/database dmap:1.0
```
