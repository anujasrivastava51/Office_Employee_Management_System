from django.contrib import admin
# from .models import Employee,Role,Department
from .models import *
# Register your models here.

admin.site.register((Employee,Role,Department))