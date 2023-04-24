from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        rating = request.POST.get('rating', 5)
        content = request.POST.get('content', '')

        if content:
            review = Review.objects.create(
                product=product,
                rating=rating,
                content=content,
                created_by=request.user
            )

            return redirect('product', slug=slug)
    
    return render(request, 'product/product.html', {'product':product})
