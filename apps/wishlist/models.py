from __future__ import unicode_literals
from django.db import models
from ..users.models import Users
from datetime import datetime

class ItemManager(models.Manager):
    def createItem(self, postData, user_id):
        response = {
            'status' : False,
            'errors' : []
        }
        if len(postData['item']) < 2:
            response['errors'].append('invalid item FRIEND')
        if len(response['errors']) == 0:
            response['status'] = True
            user_id = Users.objects.get(id = user_id)
            item = Item.objects.create(
                item = postData['item'],
                added_by = user_id
            )
            item.other.add(user_id)
            item.save()
        return response
    
    def createOther(self, user_id, item_id):
        user_id = Users.objects.get(id = user_id)
        item = Item.objects.get(id = item_id)
        item.other.add(user_id)
        item.save()
    
    def removeItem(self, user_id, item_id):
        user_id = Users.objects.get(id = user_id)
        item = Item.objects.get(id = item_id)
        item.other.remove(user_id)
        item.save()
    
    def deleteItem(self, user_id, item_id):
        item = Item.objects.get(id = item_id)
        item.delete()


class Item(models.Model):

    item = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    other = models.ManyToManyField(Users, related_name = 'other_user')
    added_by = models.ForeignKey(Users, related_name = 'added_by', null=True)
    objects = ItemManager()