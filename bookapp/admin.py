from django.contrib import admin
from . models import books,request_for_book,add_to_cart
# Register your models here.
admin.site.register(books)
admin.site.register(request_for_book)
admin.site.register(add_to_cart)

