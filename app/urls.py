from django.urls import path
from . import views as v

app_name='app'
urlpatterns = [
    path('',v.index,name='index'),
    path('<int:id>/edite', v.edite, name='edite'),
    path('<int:id>/delete', v.delete, name='delete'),

]
