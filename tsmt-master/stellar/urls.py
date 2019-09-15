from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index),
    url(r'^send/$', views.send, name='send'),
    url(r'^request/', views.request, name='request'),
    url(r'^get_contacts/', views.get_contacts, name='get_contacts'),
    url(r'^contact/$', views.contact, name='contact'),
    # url(r'^contact_delete/<id>', views.contact_delete, name='contact_delete'),
    url(r'^contact_create/', views.contact_create, name='contact_create'),
    url(r'^accountdetails/', views.accountdetails, name='accountdetails'),
    url(r'^importaccount/$', views.importaccount, name='importaccount'),
    url(r'^transactions/', views.transactions, name='transactions'),
    url(r'^offers/', views.offers, name='offers'),
    url(r'^create_account/', views.create_account, name='create_account'),
    url(r'^accounts/', views.accounts, name='accounts'),
    url(r'^get_keys/', views.keys, name='get_keys'),
    url(r'^create_fund/', views.create_fund, name='create_fund'),
    url(r'^qrcode_gen/', views.qrcode_gen, name='qrcode_gen'),
    # url(r'^accountseed', views.accountseed, name='accountseed'),
    url(r'^(?P<str_addr>[A-Z,0-9]+)/$', views.detail, name='detail'),
    path('contact_delete/<id>',views.contact_delete,name='contact_delete'),
    path('send_contact/<id>',views.send_contact,name='send_contact')
    ]
