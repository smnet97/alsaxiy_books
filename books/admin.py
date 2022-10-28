from django.contrib import admin
from . import models

admin.site.register(models.AutherModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.BookImageModel)
admin.site.register(models.TranslatorModel)
admin.site.register(models.FeaturesModel)
admin.site.register(models.PublisherModel)


@admin.register(models.BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    readonly_fields = ['real_price']