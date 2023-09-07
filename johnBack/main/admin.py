from django.contrib import admin

from main.models import Category,Product,Size,Extra





class sizeAdmin(admin.ModelAdmin):
    list_display = ['name','code']

class extraAdmin(admin.ModelAdmin):
    list_display = ['name','code']


class variantsAdmin(admin.ModelAdmin):
    list_display = ['title','product','size','extra']





admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size,sizeAdmin)
admin.site.register(Extra,extraAdmin)