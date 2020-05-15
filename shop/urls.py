from django.urls import path

from . import product
from . import productList
from . import search
from . import campaign


urlpatterns = [
	path("campaign", campaign.main),
	path("search", search.main),
    path('<section>', productList.main),
	path("<section>/<product>", product.main)]