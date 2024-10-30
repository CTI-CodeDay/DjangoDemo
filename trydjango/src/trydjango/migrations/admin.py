from django.contrib import admin # type: ignore

from models import Product

admin.state.register(Product)