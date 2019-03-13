from django.urls import path, re_path
from . import views

app_name = 'wiki'

urlpatterns = [
    # '/'
    re_path(r'^$',views.index, name='index'),

    # '/<id>'
    re_path(r'^(?P<house_id>[0-9]+)/$',views.detail, name='detail')

]
