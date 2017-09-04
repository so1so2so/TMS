from django.contrib import admin
from  tmsserver.models import Service


# Register your models here.


class CompactInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/compact.html'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('service_id','service_name', 'service_address', 'service_command')
    search_fields = ('service_id','service_name',)
    # date_hierarchy = 'service_test2'
    # ordering = ('-service_test2',)
    # fields = ('service_address','service_name',)
    # filter_horizontal = ('service_address',)
admin.site.register(Service, AuthorAdmin)
# admin.site.register(Service)
