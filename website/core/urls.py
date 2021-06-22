from django.urls import path
from .views import home, form_biblioteca, form_mod_biblioteca, form_del_biblioteca

urlpatterns = [
    path('', home, name="home"),
    path('form-biblioteca', form_biblioteca, name="form_biblioteca"),
    path('form-mod-biblioteca/<id>', form_mod_biblioteca, name="form_mod_biblioteca"),
    path('form-del-biblioteca/<id>', form_del_biblioteca, name="form_del_biblioteca"),
]