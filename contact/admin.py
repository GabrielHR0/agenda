from django.contrib import admin
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'firstName', 'lastName', 'phone', 'email'
    ordering = '-id',
    #list_filter = 'created_date'
    search_fields = 'id', 'firstName', 'lastName',
    list_per_page = 10
    list_max_show_all = 50
    list_editable = 'phone',
    list_display_links = 'id',