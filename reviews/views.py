# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib  import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core import serializers
from django.utils import simplejson
from django.db.models import Count
from forms import ReviewForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import datetime
from models import *
import datetime
# Create your views here.


def home(request):
    if request.user.is_authenticated():
        user = request.user
        prods = Product.objects.all()
        i = 0
        prodmatrix = {}
        for prod in prods:
            #                       0             1           2    3
            prodmatrix[str(i)] = [[prod.name], [prod.image], [], [prod.slug]] 
            review = Review.objects.get(product=prod.id) #   ^ this is for tags 
            for tags in review.tag.all():     #                           
                print tags.name
                prodmatrix[str(i)][2].append(tags.name) # append only tags 
            i = i + 1
        #for prod in prods:
        #    tags = Review.objects.filter(product=prod.id)
        #    for tag in tags:
        #        prodmatrix[str(i)] = [[prod.name], [prod.image], [tag]]
        #    i = i + 1    
        return render(request, 'home.html',{'prodmatrix':prodmatrix, 'prods':prods})
    else:
        products = Product.objects.all()
        
        return render(request, 'home.html',{'products':products})
        return render(request, 'home.html')
    

@login_required
def dashboard(request):
    return HttpResponseRedirect('/account/login')

def login(request):
    return HttpResponseRedirect('/account/login')

def auth_view(request):
    return render(request, 'dashboard.html')


def single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    prod = Product.objects.get(slug=slug)
    reviews = Review.objects.get(product=prod.id)
    reviewmatrix = {}
    user = request.user
    i = 0
    try:
        for rev in reviews:
            reviewmatrix[str(i)] = [[review.review_text]]
            u = User.objects.get(username=rev.user)
            i = i + 1
    except:
        u = User.objects.get(username=reviews.user)
        reviewmatrix[str(i)] = [[reviews.review_text]]
    
    if request.method=="POST":
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            user2 = get_object_or_404(User, pk=user.id)
            response = form.save(user=user2.id, product=prod.id)
            msg = 'Obrigado por avaliar ' + prod.name
        else:
            msg = 'Houve algum erro no servidor :('
        return render(request, 'product_detail.html', {'prod':prod, 'reviews':reviews, 'user':u.first_name, 'msg':msg})    
    else:    
        form = ReviewForm()    
        args = {}
        args.update(csrf(request))
    return render(request, 'product_detail.html', {'prod':prod, 'reviews':reviews, 'user':u.first_name, 'form':form})   
    #return render('product_detail.html', {'prod':prod, 'reviews':reviews, 'user':u.first_name })


def search(request):
    if 'q' in request.GET and request.POST['q']:
        message = 'You search for: %r' % request.GET['q']
        print "AEAEAE"
        return render(request, 'search.html', {'msg':message})
    else:
        message = 'You submited an empty form'
        print "AAAAAAH"
        return render(request, 'home.html', {'msg':message})