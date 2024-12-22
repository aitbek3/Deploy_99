from django.contrib import admin
from .models import Laptop, LaptopPhoto

class LaptopPhotoInline(admin.TabularInline):
    model = LaptopPhoto

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    inlines = [LaptopPhotoInline]
    list_display = ('brand', 'model', 'processor', 'ram_size', 'storage_size', 'price')
    list_filter = ('brand', 'processor')
    search_fields = ('model',)

admin.site.register(LaptopPhoto)

