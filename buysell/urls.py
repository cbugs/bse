from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'buysell'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^product/add/$', login_required(views.ProductCreate.as_view()), name='product_add'),
    url(r'^product/list/$', login_required(views.UserProductView.as_view()), name='user_product'),
    # e.g: /product/3/exit, restricted to logged in users only
    url(r'^product/(?P<pk>[0-9]+)/edit/$', login_required(views.ProductUpdate.as_view()), name='product_update'),
    # e.g: /product/3/delete, restricted to logged in users only
    url(r'^product/(?P<pk>[0-9]+)/delete/$', login_required(views.ProductDelete.as_view()), name='product_delete'),
]
