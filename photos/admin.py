from django.contrib import admin

# Register your models here.
from .models import Myphoto, Category


admin.site.register(Category)
admin.site.register(Myphoto)