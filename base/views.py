from django.shortcuts import render
from django.views import View
from.products import products
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,'templates/hello.html',{})
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
class ProductDetail(APIView):
    def get(self, request;pk):
        products=Product.objects.get(id=pk)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)
class ProductCreate(View):
    def get(self, request):
        return render(request,'templates/productCreate.html',{'form':ProductForm()})
    def post(self,request):
        form =ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')
        return render(request,'templates/productCreate.html',{'form':form})
class ProductUpdate(View):
    def get(self,request,id):
        product=Product.objects.get(id=id)
        form=ProductForm(instance=product)
        return render(request,'templates/productCreate.html',{'form':form})
    def post(self,request,id):
        product=Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/products/')
class ProductDelete(View):
    def get(self,request,id):
        product=Product.objects.get(id=id)
        product.delete
        return HttpResponseRedirect('/products/')
        
