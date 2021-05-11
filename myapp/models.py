from django.db import models

# Create your models here.

'''CREATE TABLE <table_name> (
id integer(100) primary key,
title varchar(50) not null,
description varchar(150) not null
);'''

class Todo(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)