from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product

class productDetails(View):
    def get(self, request, product_id):
        # Assuming you have a function to get product details by ID
        product = Product.objects.get(id=product_id)
        if product:
            return render(request, 'product_detail.html', {'product': product})
        else:
            return HttpResponse("Product not found", status=404)