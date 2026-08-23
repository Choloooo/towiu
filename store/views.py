from django.shortcuts import get_object_or_404, redirect, render
from .models import Hat

def home(request):
    hats = Hat.objects.all()
    return render(request, "store/home.html", {"hats": hats})

# Simple session-based cart
def add_to_cart(request, hat_id):
    hat = get_object_or_404(Hat, id=hat_id)
    cart = request.session.get('cart', {})

    if str(hat.id) in cart:
        cart[str(hat.id)] += 1
    else:
        cart[str(hat.id)] = 1

    request.session['cart'] = cart
    return redirect('home')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for hat_id, quantity in cart.items():
        hat = Hat.objects.get(id=hat_id)
        cart_items.append({
            'hat': hat,
            'quantity': quantity,
            'total_price': quantity * hat.final_price
        })
        total += quantity * hat.final_price

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def checkout(request, hat_id):
    hat = get_object_or_404(Hat, id=hat_id)
    # For simplicity, just add this hat to a cart with quantity=1
    cart = request.session.get('cart', {})
    cart[str(hat.id)] = 1
    request.session['cart'] = cart
    # Redirect to cart page
    return redirect('cart')
