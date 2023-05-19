from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'birthday')
    search_fields = ('username', 'email',)
    inlines = (BasketAdmin,)

