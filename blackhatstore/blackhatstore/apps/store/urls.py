
__authors__ = [
    'Eduardo Lujan <eduardo.lujan>',
]

from django.conf.urls import patterns, url, include
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('',
    url(_(r'^$'), 'apps.store.views.index', name='index'),
    url(_(r'^login/?$'), 'apps.store.views.login', name='login'),
    url(_(r'^register/?$'), 'apps.store.views.register', name='register'),
)