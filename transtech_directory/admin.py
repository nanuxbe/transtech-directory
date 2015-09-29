from django.contrib import admin

from .models import Category, Directory, ContactInfo, Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 0

@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('service_category',)
    inlines = [
        AddressInline,
        ContactInfoInline,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

