from django.contrib import admin

from .models import Product
from .models import Image
from .models import CampaignItem

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(CampaignItem)