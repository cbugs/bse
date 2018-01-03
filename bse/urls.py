from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # website url
    url(r'^', include('buysell.urls')),

    # accounts app for login, register, logout
    url(r'^', include('accounts.urls')),

    # admin
    url(r'^admin/', admin.site.urls),

    # reset password auth contrib urls
    url(r'^password_reset/$', password_reset, {'template_name': 'accounts/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    # /password_reset/confirm/base64_unique_id/token
    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,{'template_name': 'accounts/password_reset_confirm.html' }, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'},name='password_reset_complete'),
]

# static uploaded files media url
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

