from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from aws_backup_and_restore.tasks import backup_aws_func


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending} 
    
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    
    orders = customer.order_set.all()
    order_count =  orders.count()
    
    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/customer.html', context)

def test(request):
    test_func.delay()
    return HttpResponse('DONE')

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def backup_database(request):
    backup_aws_func.delay()
    return HttpResponse("Done")
    