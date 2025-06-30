# core/urls.py
from django.urls import path
from .views import (
    supabase_style_login,
    supabase_style_signup,
    project_list,
    project_create,
    project_update,
    employee_list,
    employee_create,
    employee_update,
)

urlpatterns = [
    path('auth/login/', supabase_style_login),
    path('auth/signup/', supabase_style_signup),

    # Project APIs
    path('projects/', project_list),  # GET
    path('projects/create/', project_create),  # POST
    path('projects/<str:project_id>/update/', project_update),  # PUT/PATCH

    # Employee APIs
    path('employees/', employee_list),  # GET
    path('employees/create/', employee_create),  # POST
    path('employees/<str:employee_id>/update/', employee_update),  # PUT/PATCH
]
