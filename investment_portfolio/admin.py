from django.contrib import admin
from investment_portfolio.models import User, FinancialInstrument, Transaction, Quote, Portfolio
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal information', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Other information', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(FinancialInstrument)
admin.site.register(Transaction)
admin.site.register(Quote)
admin.site.register(Portfolio)
