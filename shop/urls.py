from django.urls import path

from . import product
from . import productList

urlpatterns = [
    path('<section>', productList.main),
	path("<section>/<product>", product.main)
]