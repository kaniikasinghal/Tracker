from django.contrib import admin
from .models import Department, Employee, Project, Role, ProjectAssignment, HiringRequirement

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(ProjectAssignment)
admin.site.register(HiringRequirement)


# Register your models here.
