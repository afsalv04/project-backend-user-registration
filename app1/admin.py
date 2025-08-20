from django.contrib import admin
from .models import user
admin.site.register(user)


from .models import user,product
admin.site.register(product)
# Register your models here.
