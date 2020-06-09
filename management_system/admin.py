from django.contrib import admin
from .models import Resident, visitor

class OutgoingAdmin(admin.ModelAdmin):
    readonly_fields = ['reg']

class IsolatedAdmin(admin.ModelAdmin):
    readonly_fields = ['reason', 'reg', 'cameback']

admin.site.register(Resident, OutgoingAdmin)

class VisitorAdmin(admin.ModelAdmin):
    readonly_fields= ['vis_time']
admin.site.register(visitor, VisitorAdmin)


# Register your models here.
