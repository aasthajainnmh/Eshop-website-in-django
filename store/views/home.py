from django.shortcuts import render,redirect
from store.models.products import Products
from store.models.category import Category
from django.views import View

class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('homepage')
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products=None 
        categories=Category.get_all_category() 
        categoryID=request.GET.get('category')
        if categoryID:
            products=Products.get_all_products_byid(categoryID)
        else:
            products=Products.get_all_products()
        return render(request,'index.html',{'products':products,'categories':categories})





    