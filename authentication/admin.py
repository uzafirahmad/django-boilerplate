from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
class UserAdminView(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    search_fields = ('email','username')
    ordering = ('date_joined',)
    list_display=('email','username','date_joined')
    # readonly_fields=('id','email','username','date_joined')
    fieldsets = (
    ('Personal info', {'fields': ('username','email','password')}),
    ('Permissions', {'fields': ('is_admin', 'is_active')}),
)
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'password1', 'password2'),
    }),
)

admin.site.register(User,UserAdminView)