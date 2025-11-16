from django.shortcuts import render, redirect, get_object_or_404
from .models import customer
from django.shortcuts import render, redirect
from .forms import CustomerForm , UpdateCustomerForm
from django.contrib import messages

# صفحه اصلی
def home(request):
    return render(request, 'index.html')


# لیست همه کاربران
def information(request):
    information = customer.objects.all()
    return render(request, "information.html", {"information": information})


# حذف کاربر
def delete(request, user_id):
    user = get_object_or_404(customer, id=user_id)
    user.delete()
    messages.success(request, 'کاربر با موفقیت حذف شد')
    return redirect("information")


# صفحه جزئیات کاربر
def details(request, user_id):
    user = get_object_or_404(customer, id=user_id)
    return render(request, "details.html", {"object": user})
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            customer.objects.create(firstname=firstname, lastname=lastname)
            messages.success(request, 'کاربر با موفقیت اضافه شد')
            return redirect('information')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def update_customer(request, user_id):
    up_user = get_object_or_404(customer, id=user_id)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=up_user)
        if form.is_valid():
            form.save()
            return redirect('information')
    else:
        form = UpdateCustomerForm(instance=up_user)
    return render(request, 'update.html', {'form': form, 'user': up_user})