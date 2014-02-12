# -*- coding: utf-8 -*-

from django import forms
from django.forms import models
from models import Review 
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.template import RequestContext
import time

class ReviewForm(ModelForm):
        class Meta:
                model = Review        
                fields = ('review_text','tag')
        
        tag = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'teste'}), label='Descreva este produto em 1 palavra', help_text = 'separe as palavras por vírgulas')
        review_text = forms.CharField(widget = forms.Textarea(attrs={'cols':150,'rows':5}), label='O que você achou deste produto?', min_length=50, max_length=2000)
                
        def save(self, user, product, commit=True):
                # save the response object
                response = super(ReviewForm, self).save(commit=False)
                response.user = user
                response.tag = self.cleaned_data['tag']
                response.product = product
                response.review_text = self.cleaned_data['review_text']
                response.created = time.strftime("%c")
                response.updated = time.strftime("%c")
                response.save()

                return response