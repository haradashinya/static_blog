date: 2013-08-30
title: How to use South
tags: python,django


At first, You start to mange your app by --initial
- 1. python manage.py schemamigration YOUR_APP --initial
then
- 2. python manage.py migrate YOUR_APP

If you want to change columns of database, then type it.

- 3. python manage.py schemamigration --auto YOUR_APP
- 4. python manage.py migrate YOUR_APP


Enjoy happy coding!






