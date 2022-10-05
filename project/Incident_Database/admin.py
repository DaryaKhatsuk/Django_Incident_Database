from django.contrib import admin
from .models import Employees, IncidentDB


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'full_name', 'title', 'address', 'family_composition')
    list_filter = ('certificate', 'full_name')
    search_fields = ('certificate', 'full_name',)


@admin.register(IncidentDB)
class IncidentDBAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'date_of_registration', 'type_event', 'source_messages',
                    'registration_criminal_case', 'number_criminal_case', 'number_of_the_operation',
                    'registration_number_of_the_employee', 'the_scene_of_the_incident',
                    'a_brief_description_of_the_incident')
    list_filter = ('registration_number', 'type_event')
    search_fields = ('registration_number', 'type_event',)

