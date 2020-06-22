from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import bcrypt
import re


class UsersManager(models.Manager):
    def registration_validation(self, postData):
        now = datetime.now()
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['name']) < 2:
            result['errors'].append('name needs to be longer')
            print("YOU'VE GOT ERRORS")
        if len(Users.objects.filter(username = postData['username'])):
            result['errors'].append('That name already exists BUDDY')
        if (postData['password']) != postData['confirm_pw']:
            result['errors'].append("These passwords dont match FRIEND")
        if len(postData['username']) < 3:
            result['errors'].append('The user name is too short GUY')
        if len(postData['password']) < 8:
            result['errors'].append("Password must be longer than 8 characters GUY")
        if (postData['date']) > str(now):
            result['errors'].append('Hey BUDDY that date is in the future!!!')
        if len(result['errors']) == 0:
            result['status'] = True
            result['user_id'] = Users.objects.create(
                name = postData['name'],
                username = postData['username'],
                date_hired = postData['date'],
                password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            ).id
        return result

    def User_login(self, postData):
        result = {
            'status' : False,
            'errors' : []
        }
        existing = Users.objects.filter(username = postData['username'])
        if len(existing) == 0:
            result['errors'].append('Hey FRIEND this does not match')
        else:
            if bcrypt.hashpw(postData['password'].encode(),existing[0].password.encode()):
                result['status'] = True
                result['user_id'] = existing[0].id
                result['password'] = existing[0].password.id
            
        return(result)


class Users(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    date_hired = models.DateField()
    objects = UsersManager()
    def __repr__(self):
        return "<users object:{} {}>".format(self.name,  self.username)

    
           

