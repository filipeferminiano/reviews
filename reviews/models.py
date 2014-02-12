# -*- coding: utf-8 -*-

from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s' % self.name
    
class Hashtag(models.Model):
    hashtag_name = models.TextField()
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=500)
    #inserir campo imagem
    #inserir slugify na url do produto
    slug = models.SlugField(max_length=500)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='thumbs/')
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def reviews(self):
        return Review.objects.filter(product = self.pk)
    
    def __unicode__(self):
        return u'%s' % self.name
    
    
class Review(models.Model):
    user = models.ForeignKey(User, related_name="user_blog")
    tag = TaggableManager() 
    product = models.ForeignKey(Product)
    review_text = models.TextField() 
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
        
    def __unicode__(self):
        return u'%s' % self.review_text
    
    def getTags(prodid):
        return Review.objects.filter(product=prodid)