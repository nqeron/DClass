# DClass Registration

This is a test project to practice my Django. The project is aimed at creating a (mostly) functional class registration system.

## Installing and running

To install, simply clone the repository and run
```
python manage.py runserver (0.0.0.0:8000)

```
(with the port if you want to actually serve the site)

Note that you may need to alter class_reg/settings.py to include your ip address in the allowed hosts in order for it to function.

## Administration
Only admins may add / create Classes.

To create an administrative user run
```
python manage.py createsuperuser
```
