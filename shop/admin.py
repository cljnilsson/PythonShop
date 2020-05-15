from django.contrib import admin

from .models import Product
from .models import CampaignItem

admin.site.register(Product)
admin.site.register(CampaignItem)