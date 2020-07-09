from django.contrib import admin

# Register your models here.
from PRINCIPAL.models import *


class SliderAdmin(admin.ModelAdmin):
    list_display_links = listSlider
    list_display = listSlider
admin.site.register(Slider, SliderAdmin)

class BoxItemsAdmin(admin.ModelAdmin):
    list_display = listBoxItems
    list_display_links = listBoxItems
admin.site.register(BoxItem, BoxItemsAdmin)

class FeatureAdim(admin.ModelAdmin):
    list_display = listFeature
    list_display_links = listFeature
admin.site.register(Feature, FeatureAdim)



class FooterAdmin(admin.ModelAdmin):
    list_display_links = listFooter
    list_display = listFooter
admin.site.register(Footer, FooterAdmin)


class RedesSocialesAdmin(admin.ModelAdmin):
    list_display_links = listRedesSociales
    list_display = listRedesSociales
admin.site.register(RedesSociales, RedesSocialesAdmin)

