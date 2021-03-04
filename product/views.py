from django.shortcuts import render, get_object_or_404
from . models import Dress_product, Order, Electronic_product


def home(request):
    return render(request, 'home.html')


def shop(request):
    return render(request, 'shop.html')


def cloath(request):
    cloath = Dress_product.objects.all()
    return render(request, 'cloath.html', {'cloath': cloath})


def detail(request, p_id):
    detail = get_object_or_404(Dress_product, pk=p_id)
    detail.total = int(detail.price) + 1
    if detail.offer:
        detail.total = int(detail.price) + 1 - int(detail.price//detail.offer)
    if request.method == 'POST':
        order = Order()
        order.firstname = request.POST.get('first')
        order.lastname = request.POST.get('last')
        order.address = request.POST.get('add')
        order.city = request.POST.get('city')
        order.zipcode = request.POST.get('zipcode')
        order.phone = request.POST.get('phn')
        order.quantity = request.POST.get('quantity')
        order.email = request.POST.get('email')
        order.price = detail.total * int(order.quantity)
        order.size = request.POST['productsize']
        order.product = detail.description
        order.save()
        return redirect('tracking')
    else:
        return render(request, 'product-single.html', {'detail': detail})


def electronic(request):
    elect = Electronic_product.objects.all()
    return render(request, 'electronic.html', {'elect': elect})


def elect_detail(request, e_id):
    elect_detail = get_object_or_404(Electronic_product, pk=e_id)
    elect_detail.total = int(elect_detail.price) + 1
    if elect_detail.offer:
        elect_detail.total = int(elect_detail.price) + \
            1 - int(elect_detail.price//elect_detail.offer)
    if request.method == 'POST':
        order = Order()
        order.firstname = request.POST.get('first')
        order.lastname = request.POST.get('last')
        order.address = request.POST.get('add')
        order.city = request.POST.get('city')
        order.zipcode = request.POST.get('zipcode')
        order.phone = request.POST.get('phn')
        order.email = request.POST.get('email')
        order.price = elect_detail.total
        order.size = request.POST['productsize']
        order.quantity = request.POST.get('quantity')
        order.product = elect_detail.description
        order.save()
        return redirect('tracking')
    else:
        return render(request, 'elect_single.html', {'elect_detail': elect_detail})


# def tracking(request, t_id):
#     return render(request, 'tracking.html')
