from django.contrib import admin
from reviews.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Hashtag)