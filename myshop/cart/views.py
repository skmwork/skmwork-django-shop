from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from cart.session_cart import SessionCart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request, product_id):
    session_cart = SessionCart(request)
    
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        session_cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    session_cart = SessionCart(request)
    product = get_object_or_404(Product, id=product_id)
    session_cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    session_cart = SessionCart(request)
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'cart/detail.html',
                  {'cart': session_cart,
                   'coupon_apply_form': coupon_apply_form,
                   })
