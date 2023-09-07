from django.contrib import admin
from .models import Cloth, City, Colour, Collection, Brands, Sex, Style, Type, Size
# Register your models here.

class ClothAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cloth._meta.fields] #прикольная тема, надо запомнить
    #list_display = ['title', 'slug', 'description', 'colour', 'price',  'city_from', 'brand', 'collection', 'type', 'sex', 'style', 'photo' ]
    list_display_links = ['title']
    # search_fields = ('categories',)
    prepopulated_fields = {'slug':('title',)}
class CityAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']

class ColourAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']

class BrandsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']

class SexAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

class StyleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


admin.site.register(Cloth, ClothAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Size, SizeAdmin)
