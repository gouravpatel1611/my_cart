from django.contrib import admin

# Register your models here.
from .models import Product , Contect , Orders

admin.site.register(Product)
admin.site.register(Contect)
admin.site.register(Orders)