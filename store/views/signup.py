from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View




class SignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
        value={
        'first_name':first_name,
        'last_name':last_name,
        'phone':phone,
        'email':email
        }
        
        
        # validation
        error_message=None
        
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        
        error_message=self.validateCustomer(customer)
        if not error_message:
            customer.password=make_password(customer.password)
            customer.save()
            return redirect('homepage')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)       
    def validateCustomer(self,customer):
        error_message=None
        if (not customer.first_name):
            error_message='First name is required !!'
        elif len(customer.first_name)<4:
            error_message='First name must be four character long !!'
        elif (not customer.last_name):
            error_message='Last name is required !!'
        elif len(customer.last_name)<4:
            error_message='Last name must be four character long !!'
        elif not customer.phone:
            error_message='Please enter phone number'
        elif len(customer.phone)!=10:
            error_message='Please enter 10 digits phone number'
        elif not customer.email:
            error_message='Please enter the email id'
        elif customer.isExists():
            error_message='Email address already registed...'
        return error_message 
