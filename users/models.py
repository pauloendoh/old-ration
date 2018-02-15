from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Item(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    type = models.CharField(max_length=255, null=False)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(null=True)
    avg_interest = models.FloatField(null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def calc_average(self):
        self.avg_rating = self.user_items.all().aggregate(Avg('rating')).values()[0]
        self.avg_interest = self.user_items.all().aggregate(Avg('interest')).values()[0]
        self.save()

class User_Item(models.Model):
    user = models.ForeignKey(User, related_name='user_items')
    item = models.ForeignKey(Item, related_name='user_items')
    rating = models.FloatField(null=True, blank=True)
    interest = models.FloatField(null=True, blank=True)







