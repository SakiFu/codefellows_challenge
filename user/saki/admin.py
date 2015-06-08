from django.contrib import admin
from saki.models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['first_name']}),
                 (None, {'fields': ['last_name']}),
                 (None, {'fields': ['email']}),
                 (None, {'fields': ['thumbnail']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                 ]
    list_display = ('first_name', 'last_name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['first_name']

admin.site.register(User, UserAdmin)







