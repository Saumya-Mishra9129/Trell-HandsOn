# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_date_time = models.DateTimeField('date published')
    movie_director = models.CharField(max_length=200)
    number_of_tickets = models.IntegerField(default=0)
    movie_description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def add_details(self,time,price,tickets):
        self.movie_date_time = time
        self.number_of_tickets = tickets
        self.price = price

    def purchase_tickets(self,num):
        if self.number_of_tickets>num:
            self.number_of_tickets-=num
        else:
            print("Only"+str(self.number_of_tickets)+"available, Please select less tickets to purchase")

# Create your models here.
