from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Sum
from django.contrib import messages
from app1.models import Employees
from app1.models import Customer
from app1.models import Products
from app1.models import Category
from app1.models import Supplier
from app1.models import Stock

# Create your views here.


@login_required(login_url='login')
def HomePage(request):

    total_amount = Customer.objects.aggregate(total_amount=Sum('amount'))[
        'total_amount'] or 0
    emp = Employees.objects.all()
    emp_count = emp.count()
    pro = Products.objects.all()
    pro_count = pro.count()
    cat = Category.objects.all()
    cat_count = cat.count()
    context = {
        'emp': emp,
        'emp_count': emp_count,
        'pro': pro,
        'pro_count': pro_count,
        'cat': cat,
        'cat_count': cat_count,
        'total_amount': total_amount,
    }
    return render(request, 'home.html', context)


def EmpPage(request):
    emp = Employees.objects.all()
    emp_count = emp.count()
    pro = Products.objects.all()
    pro_count = pro.count()
    cat = Category.objects.all()
    cat_count = cat.count()
    context = {
        'emp': emp,
        'emp_count': emp_count,
        'pro': pro,
        'pro_count': pro_count,
        'cat': cat,
        'cat_count': cat_count,
    }
    return render(request, 'emps.html', context)


def SignupPage(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        uname_check = User.objects.filter(username=uname).exists()
        email_check = User.objects.filter(email=email).exists()

        if uname_check == True:
            messages.error(
                request, "This Kind of name is already exits,Please try different")
            return redirect('signup')

        if email_check == True:
            messages.error(
                request, "This Kind of Email is already Exits plss try differnet")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(
                request, "Your Password And Confirm Password Didn't Match")
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(
                request, "Your Account Has Been Created Successfully")
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            if user.is_active:
                login(request, user)

                if user.is_superuser:
                    # Redirect to admin dashboard for superuser
                    return redirect('home')
                else:
                    # Redirect to user dashboard for regular user
                    return redirect('emps')
            else:
                messages.error(request, 'Your account is disabled.')
        else:
            # Authentication failed, display an error message
            messages.error(
                request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def StaffPage(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'staff.html', context)


@login_required(login_url='login')
def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')

        try:
            salary_number = int(salary)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('staff')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('staff')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('staff')
        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('staff')

        if Employees.objects.filter(name=name).exists():
            messages.error(
                request, "Alert !!!Name is already Exist,Please Try Different")
            return redirect('staff')

        if Employees.objects.filter(email=email).exists():
            messages.error(
                request, "Alert !!!Email is already Exist,Please Try Different")
            return redirect('staff')

        if Employees.objects.filter(phone=phone).exists():
            messages.error(request, "Alert !!!Number is already Exist")
            return redirect('staff')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('staff')

        emp = Employees(
            name=name,
            email=email,
            address=address,
            phone=phone,
            salary=salary,
        )
        emp.save()
        return redirect('staff')
    return render(request, 'staff.html')


@login_required(login_url='login')
def Edit(request):
    emp = Employees.objects.all()

    context = {
        'emp': emp,
    }
    return redirect(request, 'staff.html', context)


@login_required(login_url='login')
def Update(request, id):
    existing_Employees = get_object_or_404(Employees, pk=id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')

        try:
            salary_number = int(salary)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('staff')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('staff')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('staff')
        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('staff')

        if Employees.objects.filter(name=name).exclude(pk=existing_Employees.pk).exists():
            messages.error(request, "person is already exist")
            return redirect('staff')

        if Employees.objects.filter(phone=phone).exclude(pk=existing_Employees.pk).exists():
            messages.error(request, "Number is already exist")
            return redirect('staff')

        if Employees.objects.filter(email=email).exclude(pk=existing_Employees.pk).exists():
            messages.error(request, "person is already exist")
            return redirect('staff')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('staff')

        emp = Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
            salary=salary,
        )
        emp.save()
        return redirect('staff')
    return redirect(request, 'staff.html')


@login_required(login_url='login')
def Delete(request, id):
    emp = Employees.objects.filter(id=id)
    emp.delete()

    context = {

        'emp': emp,
    }
    return redirect('staff')


def CustomerPage(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
    }
    return render(request, 'cust.html', context)


def AddCustomer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Brand = request.POST.get('Brand')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        invoiceNumber = request.POST.get('invoiceNumber')
        invoiceDate = request.POST.get('invoiceDate')

        try:
            invoiceNumber_number = int(invoiceNumber)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cust')

        try:
            amount_number = int(amount)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cust')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('cust')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cust')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('cust')

        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('cust')

        if not name.replace(' ', '').isalpha():
            messages.error(
                request, "Name must contain only alphabetical characters")
            return redirect('cust')

        if Customer.objects.filter(name=name).exists():
            messages.error(request, "person is already exist")
            return redirect('cust')

        if Customer.objects.filter(phone=phone).exists():
            messages.error(request, "This Number is already exist")
            return redirect('cust')

        if Customer.objects.filter(invoiceNumber=invoiceNumber).exists():
            messages.error(request, "This Invoice Number is already exist")
            return redirect('cust')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('cust')

        if len(phone) != 10:
            messages.error(request, "Number Should be 10 Digit")
            return redirect('cust')

        try:
            product = Products.objects.get(Brand=Brand)
        except Products.DoesNotExist:
            messages.error(request, f"No product found with Brand '{Brand}'")
            return redirect('cust')

        if product.quantity < quantity_number:
            messages.error(request, "Not enough quantity available")
            return redirect('cust')

        # Reduce the quantity of the associated product
        product.quantity -= quantity_number
        product.save()

        if product.quantity == 0:
            product.delete()

        cus = Customer(
            name=name,
            address=address,
            phone=phone,
            Brand=Brand,
            quantity=quantity,
            amount=amount,
            invoiceNumber=invoiceNumber,
            invoiceDate=invoiceDate,
        )
        cus.save()
        return redirect('cust')
    return render(request, 'cust.html')


def editCustomer(request):
    cus = Customer.objects.all()

    context = {
        'cus': cus,
    }
    return redirect(request, 'cust.html', context)


def updateCustomer(request, id):
    existing_customer = get_object_or_404(Customer, pk=id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Brand = request.POST.get('Brand')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        invoiceNumber = request.POST.get('invoiceNumber')
        invoiceDate = request.POST.get('invoiceDate')

        try:
            invoiceNumber_number = int(invoiceNumber)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cust')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('cust')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cust')

        try:
            amount_number = int(amount)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cust')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('cust')
        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('cust')

        if Customer.objects.filter(name=name).exclude(pk=existing_customer.pk).exists():
            messages.error(request, "person is already exist")
            return redirect('cust')

        if Customer.objects.filter(phone=phone).exclude(pk=existing_customer.pk).exists():
            messages.error(request, "Number is already exist")
            return redirect('cust')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('cust')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('cust')

        try:
            product = Products.objects.get(Brand=Brand)
        except Products.DoesNotExist:
            messages.error(request, f"No product found with Brand '{Brand}'")
            return redirect('cust')

        if product.quantity < quantity_number:
            messages.error(request, "Not enough quantity available")
            return redirect('cust')

        # Reduce the quantity of the associated product
        product.quantity -= quantity_number
        product.save()

        if product.quantity == 0:
            product.delete()

        cus = Customer(
            id=id,
            name=name,
            address=address,
            phone=phone,
            Brand=Brand,
            quantity=quantity,
            amount=amount,
            invoiceNumber=invoiceNumber,
            invoiceDate=invoiceDate,

        )
        cus.save()
        return redirect('cust')
    return redirect(request, 'cust.html')


def deleteCustomer(request, id):

    cus = Customer.objects.filter(id=id)
    cus.delete()

    context = {

        'cus': cus,
    }
    return redirect('cust')


def ProductPage(request):
    pro = Products.objects.all()

    context = {
        'pro': pro,
    }
    return render(request, 'prod.html', context)


def AddProduct(request):
    if request.method == "POST":
        colorname = request.POST.get('colorname')
        Category = request.POST.get('Category')
        Brand = request.POST.get('Brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('prod')

        if Products.objects.filter(colorname=colorname).exists():
            messages.error(
                request, "Color is already exist,Please Try Differnet")
            return redirect('prod')

        if Products.objects.filter(colorcode=colorcode).exists():
            messages.error(
                request, "Code is already exist,Please Try Different")
            return redirect('prod')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('prod')

        try:
            price_number = int(price)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('prod')

        pro = Products(
            colorname=colorname,
            Category=Category,
            Brand=Brand,
            colorcode=colorcode,
            quantity=quantity,
            price=price,
        )
        pro.save()
        return redirect('prod')
    return render(request, 'prod.html')


def editProduct(request):
    pro = Products.objects.all()

    context = {
        'pro': pro,

    }
    return redirect(request, 'prod.html', context)


def updateProduct(request, id):

    existing_product = get_object_or_404(Products, pk=id)

    if request.method == "POST":
        colorname = request.POST.get('colorname')
        Category = request.POST.get('Category')
        Brand = request.POST.get('Brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('prod')

        try:
            price_number = int(price)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('prod')

        if Products.objects.filter(colorname=colorname).exclude(pk=existing_product.pk).exists():
            messages.error(
                request, "color is already exist,please Try Different")
            return redirect('prod')

        if Products.objects.filter(colorcode=colorcode).exclude(pk=existing_product.pk).exists():
            messages.error(
                request, "code is already exist,please Try Different")
            return redirect('prod')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('prod')

        pro = Products(
            id=id,
            colorname=colorname,
            Category=Category,
            Brand=Brand,
            colorcode=colorcode,
            quantity=quantity,
            price=price,
        )
        pro.save()
        return redirect('prod')
    return redirect(request, 'prod.html')


def deleteProduct(request, id):

    pro = Products.objects.filter(id=id)
    pro.delete()

    context = {

        'pro': pro,
    }
    return redirect('prod')


def CategoryPage(request):
    cat = Category.objects.all()
    context = {
        'cat': cat,
    }
    return render(request, 'cate.html', context)


def AddCategory(request):
    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        Types = request.POST.get('Types')
        brand = request.POST.get('brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cate')

        if Category.objects.filter(categoryname=categoryname).exists():
            messages.error(
                request, "Category is already exist,Please Try Differnet")
            return redirect('cate')

        if Category.objects.filter(colorcode=colorcode).exists():
            messages.error(
                request, "Code is already exist,Please Try Different")
            return redirect('cate')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('cate')

        cat = Category(
            categoryname=categoryname,
            Types=Types,
            brand=brand,
            colorcode=colorcode,
            quantity=quantity,
        )
        cat.save()
        return redirect('cate')
    return render(request, 'cate.html')


def editCategory(request):
    cat = Category.objects.all()

    context = {
        'cat': cat,

    }
    return redirect(request, 'cate.html', context)


def updateCategory(request, id):

    existing_category = get_object_or_404(Category, pk=id)

    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        Types = request.POST.get('Types')
        brand = request.POST.get('brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cate')

        if Category.objects.filter(categoryname=categoryname).exclude(pk=existing_category.pk).exists():
            messages.error(
                request, "category is already exist,please Try Different")
            return redirect('cate')

        if Products.objects.filter(colorcode=colorcode).exclude(pk=existing_category.pk).exists():
            messages.error(
                request, "code is already exist,please Try Different")
            return redirect('cate')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('cate')

        cat = Category(
            id=id,
            categoryname=categoryname,
            Types=Types,
            brand=brand,
            colorcode=colorcode,
            quantity=quantity,

        )
        cat.save()
        return redirect('cate')
    return redirect(request, 'cate.html')


def deleteCategory(request, id):

    cat = Category.objects.filter(id=id)
    cat.delete()

    context = {

        'cat': cat,
    }
    return redirect('cate')


def SupplierPage(request):
    sup = Supplier.objects.all()
    context = {

        'sup': sup,
    }
    return render(request, 'sup.html', context)


def AddSupplier(request):
    if request.method == "POST":
        suppliercode = request.POST.get('suppliercode')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        website = request.POST.get('website')
        Notes = request.POST.get('Notes')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('sup')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('sup')
        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('sup')

        if Supplier.objects.filter(suppliercode=suppliercode).exists():
            messages.error(
                request, "suppliercode is already exist,Please Try Different")
            return redirect('sup')

        if Supplier.objects.filter(email=email).exists():
            messages.error(
                request, "Email is already exist,Please Try Different")
            return redirect('sup')

        if Supplier.objects.filter(name=name).exists():
            messages.error(
                request, "person is already exist,Please Try Different")
            return redirect('sup')

        if Supplier.objects.filter(phone=phone).exists():
            messages.error(
                request, "This Number is already exist,Please Try Different")
            return redirect('sup')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('sup')

        sup = Supplier(
            suppliercode=suppliercode,
            name=name,
            address=address,
            phone=phone,
            email=email,
            website=website,
            Notes=Notes,
        )
        sup.save()
        return redirect('sup')
    return render(request, 'sup.html')


def editSupplier(request):
    sup = Supplier.objects.all()

    context = {
        'sup': sup,

    }
    return redirect(request, 'sup.html', context)


def updateSupplier(request, id):
    existing_Supplier = get_object_or_404(Supplier, pk=id)

    if request.method == "POST":
        suppliercode = request.POST.get('suppliercode')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        website = request.POST.get('website')
        Notes = request.POST.get('Notes')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('sup')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('sup')
        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('sup')

        if Supplier.objects.filter(suppliercode=suppliercode).exclude(pk=existing_Supplier.pk).exists():
            messages.error(
                request, "category is already exist,please Try Different")
            return redirect('sup')

        if Supplier.objects.filter(name=name).exclude(pk=existing_Supplier.pk).exists():
            messages.error(
                request, "name is already exist,please Try Different")
            return redirect('sup')

        if Supplier.objects.filter(email=email).exclude(pk=existing_Supplier.pk).exists():
            messages.error(
                request, "Email is already exist,please Try Different")
            return redirect('sup')

        if Supplier.objects.filter(phone=phone).exclude(pk=existing_Supplier.pk).exists():
            messages.error(
                request, "Number is already exist,please Try Different")
            return redirect('sup')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('sup')

        sup = Supplier(
            id=id,
            suppliercode=suppliercode,
            name=name,
            address=address,
            phone=phone,
            email=email,
            website=website,
            Notes=Notes,
        )

        sup.save()
        return redirect('sup')
    return render(request, 'sup.html')


def deleteSupplier(request, id):

    sup = Supplier.objects.filter(id=id)
    sup.delete()

    context = {

        'sup': sup,
    }
    return redirect('sup')


def StockPage(request):
    stk = Stock.objects.all()
    context = {

        'stk': stk,
    }
    return render(request, 'stk.html', context)


def AddStock(request):
    if request.method == "POST":
        Items = request.POST.get('Items')
        category = request.POST.get('category')
        Brand = request.POST.get('Brand')
        Status = request.POST.get('Status')
        sellingprice = request.POST.get('sellingprice')

        try:
            sellingprice_number = int(sellingprice)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('stk')

        if Stock.objects.filter(Items=Items).exists():
            messages.error(
                request, "Item is already exist,Please Try Different")
            return redirect('stk')

        if Stock.objects.filter(category=category).exists():
            messages.error(
                request, "category is already exist,Please Try Different")
            return redirect('stk')

        if Stock.objects.filter(Brand=Brand).exists():
            messages.error(
                request, "Brand is already exist,Please Try Different")
            return redirect('stk')

        stk = Stock(
            Items=Items,
            category=category,
            Brand=Brand,
            Status=Status,
            sellingprice=sellingprice,

        )
        stk.save()
        return redirect('stk')
    return render(request, 'stk.html')


def editStock(request):
    stk = Stock.objects.all()

    context = {
        'stk': stk,

    }
    return redirect(request, 'stk.html', context)


def updateStock(request, id):
    existing_Stock = get_object_or_404(Stock, pk=id)
    if request.method == "POST":
        Items = request.POST.get('Items')
        category = request.POST.get('category')
        Brand = request.POST.get('Brand')
        Status = request.POST.get('Status')
        sellingprice = request.POST.get('sellingprice')

        try:
            sellingprice_number = int(sellingprice)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('stk')

        if Stock.objects.filter(Items=Items).exclude(pk=existing_Stock.pk).exists():
            messages.error(
                request, "Items is already exist,please Try Different")
            return redirect('stk')

        if Stock.objects.filter(category=category).exclude(pk=existing_Stock.pk).exists():
            messages.error(
                request, "category is already exist,please Try Different")
            return redirect('stk')

        if Stock.objects.filter(Brand=Brand).exclude(pk=existing_Stock.pk).exists():
            messages.error(
                request, "Brand is already exist,please Try Different")
            return redirect('stk')

        stk = Stock(
            id=id,
            Items=Items,
            category=category,
            Brand=Brand,
            Status=Status,
            sellingprice=sellingprice,

        )
        stk.save()
        return redirect('stk')
    return render(request, 'stk.html')


def deleteStock(request, id):

    stk = Stock.objects.filter(id=id)
    stk.delete()

    context = {

        'stk': stk,
    }
    return redirect('stk')


def customerpage(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
    }
    return render(request, 'custo.html', context)


def Addcustomer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Brand = request.POST.get('Brand')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        invoiceNumber = request.POST.get('invoiceNumber')
        invoiceDate = request.POST.get('invoiceDate')

        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('custo')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('custo')

        try:
            amount_number = int(amount)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('custo')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('custo')

        if not name.isalpha():
            messages.error(
                request, "Name must contain only alphabetical characters")
            return redirect('custo')

        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('custo')

        if Customer.objects.filter(name=name).exists():
            messages.error(
                request, "Customer name is already exist,Please Try Different")
            return redirect('custo')

        if Customer.objects.filter(phone=phone).exists():
            messages.error(
                request, "Number is already exist,Please Try Different")
            return redirect('custo')

        if Customer.objects.filter(invoiceNumber=invoiceNumber).exists():
            messages.error(
                request, "Number is already exist,Please Try Different")
            return redirect('custo')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('custo')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('custo')

        try:
            product = Products.objects.get(Brand=Brand)
        except Products.DoesNotExist:
            messages.error(request, f"No product found with Brand '{Brand}'")
            return redirect('custo')

        if product.quantity < quantity_number:
            messages.error(request, "Not enough quantity available")
            return redirect('custo')

        # Reduce the quantity of the associated product
        product.quantity -= quantity_number
        product.save()

        if product.quantity == 0:
            product.delete()

        cus = Customer(
            name=name,
            address=address,
            phone=phone,
            Brand=Brand,
            quantity=quantity,
            amount=amount,
            invoiceNumber=invoiceNumber,
            invoiceDate=invoiceDate,
        )
        cus.save()
        return redirect('custo')
    return render(request, 'custo.html')


def editcustomer(request):
    cus = Customer.objects.all()

    context = {
        'cus': cus,
    }
    return redirect(request, 'custo.html', context)


def updatecustomer(request, id):
    existing_customer = get_object_or_404(Customer, pk=id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Brand = request.POST.get('Brand')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        invoiceNumber = request.POST.get('invoiceNumber')
        invoiceDate = request.POST.get('invoiceDate')
        try:
            phone_number = int(phone)

        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('custo')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('custo')

        try:
            amount_number = int(amount)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('custo')

        phone_number = phone
        try:
            phone_number = int(''.join(c for c in phone if c.isdigit()))
        except ValueError:
            messages.error(request, "Please Enter a valid phone number")
            return redirect('custo')
        if not str(phone_number).startswith(('9', '8', '7', '6')):
            messages.error(
                request, "Invalid phone number. Please provide a number starting with 9, 8, 7, or 6.")
            return redirect('custo')

        if Customer.objects.filter(name=name).exclude(pk=existing_customer.pk).exists():
            messages.error(request, "person is already exist")
            return redirect('custo')

        if Customer.objects.filter(phone=phone).exclude(pk=existing_customer.pk).exists():
            messages.error(request, "Number is already exist")
            return redirect('custo')

        if Customer.objects.filter(invoiceNumber=invoiceNumber).exclude(pk=existing_customer.pk).exists():
            messages.error(request, "InvoiceNumber is already exist")
            return redirect('custo')

        if len(phone) != 10:
            messages.error(request, "Alert !!!Number Should be 10 Digit")
            return redirect('custo')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('custo')

        try:
            product = Products.objects.get(Brand=Brand)
        except Products.DoesNotExist:
            messages.error(request, f"No product found with Brand '{Brand}'")
            return redirect('custo')

        if product.quantity < quantity_number:
            messages.error(request, "Not enough quantity available")
            return redirect('custo')

        # Reduce the quantity of the associated product
        product.quantity -= quantity_number
        product.save()

        if product.quantity == 0:
            product.delete()

        cus = Customer(
            id=id,
            name=name,
            address=address,
            phone=phone,
            Brand=Brand,
            quantity=quantity,
            amount=amount,
            invoiceNumber=invoiceNumber,
            invoiceDate=invoiceDate,
        )
        cus.save()
        return redirect('cust')
    return redirect(request, 'custo.html')


def deletecustomer(request, id):

    cus = Customer.objects.filter(id=id)
    cus.delete()

    context = {

        'cus': cus,
    }
    return redirect('custo')


def categorypage(request):
    cat = Category.objects.all()
    context = {
        'cat': cat,
    }
    return render(request, 'cat.html', context)


def Addcategory(request):
    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        Types = request.POST.get('Types')
        brand = request.POST.get('brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cat')

        if Category.objects.filter(categoryname=categoryname).exists():
            messages.error(
                request, "Category is already exist,Please Try Differnet")
            return redirect('cat')

        if Category.objects.filter(colorcode=colorcode).exists():
            messages.error(
                request, "Code is already exist,Please Try Different")
            return redirect('cat')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('cat')

        cat = Category(
            categoryname=categoryname,
            Types=Types,
            brand=brand,
            colorcode=colorcode,
            quantity=quantity,
        )
        cat.save()
        return redirect('cat')
    return render(request, 'cat.html')


def editcategory(request):
    cat = Category.objects.all()

    context = {
        'cat': cat,

    }
    return redirect(request, 'cat.html', context)


def updatecategory(request, id):
    existing_category = get_object_or_404(Category, pk=id)
    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        Types = request.POST.get('Types')
        brand = request.POST.get('brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('cat')

        if Category.objects.filter(categoryname=categoryname).exclude(pk=existing_category.pk).exists():
            messages.error(
                request, "category is already exist,please Try Different")
            return redirect('cat')

        if Products.objects.filter(colorcode=colorcode).exclude(pk=existing_category.pk).exists():
            messages.error(
                request, "code is already exist,please Try Different")
            return redirect('cat')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('cat')

        cat = Category(
            id=id,
            categoryname=categoryname,
            Types=Types,
            brand=brand,
            colorcode=colorcode,
            quantity=quantity,

        )
        cat.save()
        return redirect('cate')
    return redirect(request, 'cat.html')


def deletecategory(request, id):

    cat = Category.objects.filter(id=id)
    cat.delete()

    context = {

        'cat': cat,
    }
    return redirect('cat')


def productpage(request):
    pro = Products.objects.all()

    context = {
        'pro': pro,
    }
    return render(request, 'pro.html', context)


def Addproduct(request):
    if request.method == "POST":
        colorname = request.POST.get('colorname')
        Category = request.POST.get('Category')
        Brand = request.POST.get('Brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('pro')

        if Products.objects.filter(colorname=colorname).exists():
            messages.error(
                request, "Color is already exist,Please Try Differnet")
            return redirect('pro')

        if Products.objects.filter(colorcode=colorcode).exists():
            messages.error(
                request, "Code is already exist,Please Try Different")
            return redirect('pro')

        try:
            price_number = int(price)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('pro')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('pro')

        pro = Products(
            colorname=colorname,
            Category=Category,
            Brand=Brand,
            colorcode=colorcode,
            quantity=quantity,
            price=price,
        )
        pro.save()
        return redirect('pro')
    return render(request, 'pro.html')


def editproduct(request):
    pro = Products.objects.all()

    context = {
        'pro': pro,

    }
    return redirect(request, 'pro.html', context)


def updateproduct(request, id):
    existing_product = get_object_or_404(Products, pk=id)
    if request.method == "POST":
        colorname = request.POST.get('colorname')
        Category = request.POST.get('Category')
        Brand = request.POST.get('Brand')
        colorcode = request.POST.get('colorcode')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            quantity_number = int(quantity)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('prod')

        try:
            price_number = int(price)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('pro')

        if Products.objects.filter(colorname=colorname).exclude(pk=existing_product.pk).exists():
            messages.error(
                request, "color is already exist,please Try Different")
            return redirect('pro')

        if Products.objects.filter(colorcode=colorcode).exclude(pk=existing_product.pk).exists():
            messages.error(
                request, "code is already exist,please Try Different")
            return redirect('pro')

        if quantity_number <= 0:
            messages.error(request, "Quantity must be greater than 0")
            return redirect('pro')

        pro = Products(
            id=id,
            colorname=colorname,
            Category=Category,
            Brand=Brand,
            colorcode=colorcode,
            quantity=quantity,
            price=price,
        )
        pro.save()
        return redirect('prod')
    return redirect(request, 'pro.html')


def deleteproduct(request, id):

    pro = Products.objects.filter(id=id)
    pro.delete()

    context = {

        'pro': pro,
    }
    return redirect('pro')


def stockpage(request):
    stk = Stock.objects.all()
    context = {

        'stk': stk,
    }
    return render(request, 'stok.html', context)


def Addstock(request):
    if request.method == "POST":
        Items = request.POST.get('Items')
        category = request.POST.get('category')
        Brand = request.POST.get('Brand')
        Status = request.POST.get('Status')
        sellingprice = request.POST.get('sellingprice')

        try:
            sellingprice_number = int(sellingprice)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('stok')

        if Stock.objects.filter(Items=Items).exists():
            messages.error(
                request, "Item is already exist,Please Try Different")
            return redirect('stok')

        if Stock.objects.filter(category=category).exists():
            messages.error(
                request, "category is already exist,Please Try Different")
            return redirect('stok')

        if Stock.objects.filter(Brand=Brand).exists():
            messages.error(
                request, "Brand is already exist,Please Try Different")
            return redirect('stok')

        stk = Stock(
            Items=Items,
            category=category,
            Brand=Brand,
            Status=Status,
            sellingprice=sellingprice,

        )
        stk.save()
        return redirect('stok')
    return render(request, 'stok.html')


def editstock(request):
    stk = Stock.objects.all()

    context = {
        'stk': stk,

    }
    return redirect(request, 'stok.html', context)


def updatestock(request, id):
    existing_Stock = get_object_or_404(Stock, pk=id)
    if request.method == "POST":
        Items = request.POST.get('Items')
        category = request.POST.get('category')
        Brand = request.POST.get('Brand')
        Status = request.POST.get('Status')
        sellingprice = request.POST.get('sellingprice')

        try:
            sellingprice_number = int(sellingprice)

        except ValueError:
            messages.error(request, "Please Enter a only numeric value")
            return redirect('stok')

        if Stock.objects.filter(Items=Items).exclude(pk=existing_Stock.pk).exists():
            messages.error(
                request, "Items is already exist,please Try Different")
            return redirect('stok')

        if Stock.objects.filter(category=category).exclude(pk=existing_Stock.pk).exists():
            messages.error(
                request, "category is already exist,please Try Different")
            return redirect('stok')

        if Stock.objects.filter(Brand=Brand).exclude(pk=existing_Stock.pk).exists():
            messages.error(
                request, "Brand is already exist,please Try Different")
            return redirect('stok')

        stk = Stock(
            id=id,
            Items=Items,
            category=category,
            Brand=Brand,
            Status=Status,
            sellingprice=sellingprice,

        )
        stk.save()
        return redirect('stok')
    return render(request, 'stok.html')


def deletestock(request, id):

    stk = Stock.objects.filter(id=id)
    stk.delete()

    context = {

        'stk': stk,
    }
    return redirect('stok')


def invoice_page(request):
    if request.method == "GET":
        name = request.GET.get('name', 'Default Name')
        address = request.GET.get('address', 'Default Address')
        phone = request.GET.get('phone', 'Default Phone')
        product = request.GET.get('product', 'Default Product')
        quantity = request.GET.get('quantity', 'Default Quantity')
        amount = request.GET.get('amount', 'Default Amount')
        invoiceNumber = request.GET.get(
            'invoiceNumber', 'Default InvoiceNumber ')
        invoiceDate = request.GET.get('invoiceDate', 'Default InvoiceDate')

        context = {
            'name': name,
            'address': address,
            'phone': phone,
            'product': product,
            'quantity': quantity,
            'amount': amount,
            'invoiceNumber': invoiceNumber,
            'invoiceDate': invoiceDate,

        }
        return render(request, 'invoice.html', context)
    return redirect('invoice')


def bill_page(request):
    if request.method == "GET":
        name = request.GET.get('name', 'Default Name')
        address = request.GET.get('address', 'Default Address')
        phone = request.GET.get('phone', 'Default Phone')
        product = request.GET.get('product', 'Default Product')
        quantity = request.GET.get('quantity', 'Default Quantity')
        amount = request.GET.get('amount', 'Default Amount')
        invoiceNumber = request.GET.get(
            'invoiceNumber', 'Default InvoiceNumber ')
        invoiceDate = request.GET.get('invoiceDate', 'Default InvoiceDate')

        context = {
            'name': name,
            'address': address,
            'phone': phone,
            'product': product,
            'quantity': quantity,
            'amount': amount,
            'invoiceNumber': invoiceNumber,
            'invoiceDate': invoiceDate,
        }
        return render(request, 'bill.html', context)
    return redirect('bill')


def monthly_sales_report(request):
    current_date = datetime.now()
    start_date = current_date.replace(
        day=1, hour=0, minute=0, second=0, microsecond=0)
    end_date = start_date + timedelta(days=31)

    # Sales Data
    product_data = Products.objects.values('colorname').annotate(
        total_sales=Sum('price'),
        total_quantity_sold=Sum('quantity')
    )

    purchases_data = Products.objects.filter(
    ).values('Category', 'Brand').annotate(
        total_purchase=Sum('price')
    )
    report_data = {
        'now': current_date,
        'start_date': start_date,
        'end_date': end_date-timedelta(days=1),
        'products_data': product_data,
        'purchases_data': purchases_data,
    }

    return render(request, 'monthly_sales_report.html',  {'report_data': report_data})


def daily_transactions(request):

    current_date = datetime.now().date()

    start_of_day = datetime.combine(current_date, datetime.min.time())
    end_of_day = datetime.combine(current_date, datetime.max.time())

    customer_transactions = Customer.objects.filter(
        invoiceDate__range=(start_of_day, end_of_day))

    total_amount = Customer.objects.aggregate(total_amount=Sum('amount'))[
        'total_amount'] or 0

    return render(request, 'daily_transactions.html', {'total_amount': total_amount})
