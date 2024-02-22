from django.contrib import admin
from django.urls import path 
from rail_ticket_application import views
from .views import generate_pdf

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('home',views.home),
    path('pnr',views.check_PNR),
    path('chart',views.chart),
    path('search',views.search),
    path('book_ticket',views.book_ticket),
    path('confirm_ticket',views.confirm_ticket),
    path('print_ticket',views.print_ticket),
    path('generate_pdf', generate_pdf, name='generate_pdf'),
    path('login',views.login),
    path('register',views.register),
    path('logout',views.logout),
]

