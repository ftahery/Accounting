from django.conf.urls import url
from . import views

app_name='accountingApp'

urlpatterns=[
    url(r'^$',views.Index.as_view(), name='index'),
    url(r'^invoice/$',views.Invoice.as_view(), name='invoice'),
    url(r'^inventory/$',views.Inventory.as_view(), name='inventory'),
    url(r'^dashboard/orders/$',views.Dashboard.as_view(), name='dashboard'),
    url(r'^dashboard/items/$',views.Items.as_view(), name='items'),
    url(r'^customers/$',views.Customers.as_view(), name='customers'),
    url(r'^about/$',views.About.as_view(), name='about'),
]

