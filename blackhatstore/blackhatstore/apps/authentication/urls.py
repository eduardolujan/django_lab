from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (RedirectView, TemplateView)

from .views import (CreateAccount,)



urlpatterns = [
    url(r'^register/$', CreateAccount.as_view(), name='register'),
]
