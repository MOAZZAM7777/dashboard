"""
URL configuration for paintsolve project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    # authentication
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    # main content
    path('home/', views.HomePage, name='home'),
    path('emps/', views.EmpPage, name='emps'),
    path('logout/', views.LogoutPage, name='logout'),
    path('staff/', views.StaffPage, name='staff'),
    path('add-employee/', views.ADD, name='add-employee'),
    path('edit-employee/', views.Edit, name='edit-employee'),
    path('update-employee/<str:id>', views.Update, name='update-employee'),
    path('delete-employee/<str:id>', views.Delete, name='delete-employee'),
    path('cust/', views.CustomerPage, name='cust'),
    path('add-customer', views.AddCustomer, name='add-customer'),
    path('edit-customer', views.editCustomer, name='edit-customer'),
    path('update-customer/<str:id>', views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:id>', views.deleteCustomer, name='delete-customer'),
    path('prod/', views.ProductPage, name='prod'),
    path('add-product', views.AddProduct, name='add-product'),
    path('edit-product', views.editProduct, name='edit-product'),
    path('update-product/<str:id>', views.updateProduct, name='update-product'),
    path('delete-product/<str:id>', views.deleteProduct, name='delete-product'),
    path('cate/', views.CategoryPage, name='cate'),
    path('add-category', views.AddCategory, name='add-category'),
    path('edit-category', views.editCategory, name='edit-category'),
    path('update-category/<str:id>', views.updateCategory, name='update-category'),
    path('delete-category/<str:id>', views.deleteCategory, name='delete-category'),
    path('sup/', views.SupplierPage, name='sup'),
    path('add-supplier', views.AddSupplier, name='add-supplier'),
    path('edit-supplier', views.editSupplier, name='edit-supplier'),
    path('update-supplier/<str:id>', views.updateSupplier, name='update-supplier'),
    path('delete-supplier/<str:id>', views.deleteSupplier, name='delete-supplier'),
    path('stk/', views.StockPage, name='stk'),
    path('add-stock', views.AddStock, name='add-stock'),
    path('edit-stock', views.editStock, name='edit-stock'),
    path('update-stock/<str:id>', views.updateStock, name='update-stock'),
    path('delete-stock/<str:id>', views.deleteStock, name='delete-stock'),
    path('custo/', views.customerpage, name='custo'),
    path('addcustomer', views.Addcustomer, name='addcustomer'),
    path('editcustomer', views.editcustomer, name='editcustomer'),
    path('updatecustomer/<str:id>', views.updatecustomer, name='updatecustomer'),
    path('deletecustomer/<str:id>', views.deletecustomer, name='deletecustomer'),
    path('cat/', views.categorypage, name='cat'),
    path('addcategory', views.Addcategory, name='addcategory'),
    path('editcategory', views.editcategory, name='editcategory'),
    path('updatecategory/<str:id>', views.updatecategory, name='updatecategory'),
    path('deletecategory/<str:id>', views.deletecategory, name='deletecategory'),
    path('pro/', views.productpage, name='pro'),
    path('addproduct', views.Addproduct, name='addproduct'),
    path('editproduct', views.editproduct, name='editproduct'),
    path('updateproduct/<str:id>', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<str:id>', views.deleteproduct, name='deleteproduct'),
    path('stok/', views.stockpage, name='stok'),
    path('addstock', views.Addstock, name='addstock'),
    path('editstock', views.editstock, name='editstock'),
    path('updatestock/<str:id>', views.updatestock, name='updatestock'),
    path('deletestock/<str:id>', views.deletestock, name='deletestock'),
    path('invoice/', views.invoice_page, name='invoice'),
    path('bill/', views.bill_page, name='bill'),
    path('monthly-sales-report/', views. monthly_sales_report,
         name='monthly_sales_report'),
    path('daily_transactions/', views.daily_transactions,
         name='daily_transactions'),






]
