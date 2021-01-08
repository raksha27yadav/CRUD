from django.urls import path
from . import views
urlpatterns = [
    path('', views.CredentialForm,name="credform"),
    path('<int:id>/', views.CredentialForm,name="credupdate"),
    path('delete/<int:id>/', views.creddelete,name="creddelete"),

    path('list/',views.credList,name="credlist"),
]
