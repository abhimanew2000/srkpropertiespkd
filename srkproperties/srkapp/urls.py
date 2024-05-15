from django.urls import path,include
from .import views
app_name = 'SRKAPP'

urlpatterns = [
    path('',views.index,name='index'),
    path('productpage/',views.productpage,name='productpage'),
    path('productdetails/<int:idn>/',views.productdetails,name='productdetails'),
    path('house',views.house,name='house'),
    path('search/',views.search,name='search'),
    path('coconut',views.coconut,name='coconut'),
    path('plot',views.plot,name='plot'),
    path('commercialproperty',views.commercialproperty,name='commercialproperty'),
    path('seller_login',views.seller_login,name='seller_login'),
    path('seller_dashboard',views.seller_dashboard,name='sdashboard'),
    path('addproduct',views.addpdt,name='addpdt'),
    path('logout',views.logout,name='logout'),
    path('email',views.email,name='email'),
    path('contact',views.contact,name='contact'),
    path('pdt_update/<int:pid>/', views.update_pdt, name='update_pdt'),
    path('pdt_delete/<int:pid>',views.pdt_delete,name='pdt_delete')



]