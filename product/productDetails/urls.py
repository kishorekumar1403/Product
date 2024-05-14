from django.urls import path
from . import views

urlpatterns =[
    path('superadmin', views.superAdminView.as_view()),
    path('superadmin/<id>', views.superAdminView.as_view()),
    path('admin', views.adminView.as_view()),
    path('admin/<id>', views.adminView.as_view()),
    path('user', views.userView.as_view()),
    path('user/<id>', views.userView.as_view()),
    path('product', views.productView.as_view()),
    path('product/<id>', views.productView.as_view()),

    path('filter', views.ProductListView.as_view()),
    path('pagination', views.productPaginationView.as_view()),

    path('superadminlogin', views.superAdminLogin.as_view()),
    path('userlogin', views.userLogin.as_view()),
    path('adminlogin', views.adminLogin.as_view())
]