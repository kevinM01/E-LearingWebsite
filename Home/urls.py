from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('login', views.loginU,name = 'login'),
    path('logout', views.logoutU,name = 'logout'),
    path('login1.html', views.login1,name = 'login1'),
    path('', views.index,name = 'index'),
    path('aboutus', views.aboutus,name = 'aboutus'),
    path('catalog', views.catalog,name = 'catalog'),
    path('contactus', views.contactus,name = 'contactus'),
    path('c1.html', views.c1,name = 'c1.html'),
    path('c2.html', views.c2,name = 'c2.html'),
    path('c3.html', views.c3,name = 'c3.html'),
    path('c4.html', views.c4,name = 'c4.html'),
    path('c5.html', views.c5,name = 'c5.html'),
    path('c6.html', views.c6,name = 'c6.html'),

]
