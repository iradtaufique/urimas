from django.contrib import admin
from urimasapp.models import User, Mission, Role, Report, Transport, Department, Category, Supervisor, School


class DisplayFields(admin.ModelAdmin):

    list_display = ['owner',
                    'role',
                    'category',
                    'department',
                    'mission_purpose',
                    'mission_result',
                    'mission_destination',
                    'distance',
                    'departure_date',
                    'returning_date',
                    'mission_duration',
                    'transport',
                    'invitation']


class DisplayFields_for_Dept(admin.ModelAdmin):
    list_display = ['name', 'category']


class DisplayFields_for_Role(admin.ModelAdmin):
    list_display = ['name', 'category']


class DisplayFields_for_Report(admin.ModelAdmin):
    list_display = ['note', 'owner', 'file']


admin.site.register(Mission, DisplayFields)
admin.site.register(Supervisor)
admin.site.register(User)
admin.site.register(Role,DisplayFields_for_Role)
admin.site.register(Report, DisplayFields_for_Report)
admin.site.register(Transport)
admin.site.register(Department, DisplayFields_for_Dept)
admin.site.register(Category)
admin.site.register(School)

