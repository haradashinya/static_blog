date: 2013-08-30
title: How to use South
tags: python,django

Recently , I've been looking for db migration tool.
and I found South Library which is db migration tool for Django.



At first, You start to mange your app by --initial

    python manage.py schemamigration YOUR_APP --initial
    python manage.py migrate YOUR_APP

If you want to change columns of database, then type it.

    python manage.py schemamigration --auto YOUR_APP
    python manage.py migrate YOUR_APP


Enjoy happy coding!






