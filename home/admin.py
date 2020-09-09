from django.contrib import admin
from .models import Books, Demo, Test

admin.site.register(Demo)
admin.site.register(Books)
admin.site.register(Test)

# Register your models here.
