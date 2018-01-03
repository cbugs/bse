from django.conf.urls import url
from accounts.views import login_view, register_view, logout_view

app_name = 'accounts'

urlpatterns = [
    # login page
    url(r'^login/', login_view, name="login"),
    # logout page
    url(r'^logout/', logout_view, name="logout"),
    # register page
    url(r'^register/', register_view, name="register"),
]