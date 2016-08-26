# MX Hacks Back End

This repository contains the source code of the API used on the application process.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the project and how to install them

* Python 3
* PIP
* Virtual Env (Virtualenvwrapper will be ideal)
* Secret variables used.
* PostgreSQL


### Installing

Create a database and user.

Install python dependencies by running:

```
pip install -r requirements/dev.txt
```

Add the secret variables to the environment following the UNIX convention:

```
export SUPER_SECRET_VARIABLE=''
```

## Built With

* [Django 1.10](https://www.djangoproject.com/)
* [Django Environ 0.4.0](https://github.com/joke2k/django-environ)
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Mailgun](https://mailgun.com/app/dashboard)

## Authors

* [**Pablo Trinidad**](https://github.com/pablotrinidad) - [Inventive](https://inventivehack.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## What's next?

* Registration system
* Push notifications integration
