from django.contrib import admin
from .models import user
admin.site.register(user)


from .models import user,Product
admin.site.register(Product)
# Register your models here.
