from django.contrib import admin

from .models import Category, Directory, ContactInfo, Address


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass