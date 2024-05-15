from django.shortcuts import render,redirect,get_object_or_404
from .models import product_tbl,Seller
from django.http import HttpResponse
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.conf import settings


# Create your views here.

def index(request):
    obj = product_tbl.objects.all()[:8]
    if obj:
        return render(request,'index.html',{"data":obj})
    else:
        return render(request,'index.html')
    
    

def productpage(request):
    obj = product_tbl.objects.all()
    if obj:
        return render(request,'productpage.html',{"data":obj})
    else:
        return render(request,'productpage.html')

def productdetails(request,idn):
    obj = product_tbl.objects.filter(id=idn)

    return render(request,'productdetails.html',{"data":obj})

def contact(request):
    return render(request,'contact.html')


#enquiry button function 
def email(request,idn):
    if request.method == 'POST':
        proname = request.POST['pronam']
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        num = request.POST['number']
        email_message = f"Name : {name}\nEmail : {email}\nNumber:{num}\n\n{message} \nProperty Name:{proname}"
        send_mail(
            'Contact Form',
            email_message,
            'setting.EMAIL_HOST_USER',
            ['renjithsiva123@gmail.com'],
            fail_silently=False

        )
    return render(request,'index.html')


# def apartment(request):
#     obj = product_tbl.objects.filter(property_type__iexact='apartment')
#     return render(request,"category.html",{"data":obj})

#category portion starts
def house(request):
    obj = product_tbl.objects.filter(property_type__iexact='house')
    return render(request,"category.html",{"data":obj})

def coconut(request):
    obj = product_tbl.objects.filter(property_type__iexact='coconut field')
    return render(request,"category.html",{"data":obj})

def commercialproperty(request):
    obj = product_tbl.objects.filter(property_type__iexact='commercial property')
    return render(request,"category.html",{"data":obj})

def plot(request):
    obj = product_tbl.objects.filter(property_type__iexact='emptyland')
    return render(request,"category.html",{"data":obj})
#category portion ends


#search function

def search(request):
    query = request.GET.get("keyword")

    # Check if the query is not empty
    if query:
        products = product_tbl.objects.filter(
            Q(property_name__icontains=query) |  # Case-insensitive containment check
            Q(property_type__icontains=query) |
            Q(price__icontains=query) |
            Q(address__icontains=query)
        )

        return render(request, "category.html", {'query': query, 'data': products})

    # If query is empty, handle it here (e.g., display a message or redirect)
    return render(request, "category.html", {'query': query, 'data': None})


#seller login 
def seller_login(request):
    if request.method=='POST':
        eml=request.POST['email1']
        pwd=request.POST['password1']
        if Seller.objects.filter(email=eml,password=pwd):
            return redirect('SRKAPP:sdashboard')
            # return render(request,'sdashboard.html')

    return render(request,'login.html')

def logout(request):
    authlogout(request)
    return redirect('/seller_login') 

#seller dashboard 
@login_required(login_url='SRKAPP:seller_login')
def seller_dashboard(request):
    pdt=product_tbl.objects.all()
    return render(request,'sdashboard.html',{'data':pdt})

#seller add propduct function
def addpdt(request):
    if request.method == 'POST':
        pname = request.POST.get('name')
        ptype = request.POST.get('type')
        pdimension = request.POST.get('pdimen')
        pprice = request.POST.get('price')
        paddress = request.POST.get('add')
        posses = request.POST.get('poss')
        pdescription = request.POST.get('description')

        # Get a list of uploaded images
        uploaded_images = []
        for i in range(1, 9):  # Assuming image fields are named image1, image2, ..., image8
            image_key = f'image{i}'
            if image_key in request.FILES:
                uploaded_images.append(request.FILES.get(image_key))

        # Create product instance and save
        product = product_tbl(
            property_name=pname,
            property_type=ptype,
            dimension=pdimension,
            address=paddress,
            possession=posses,
            description=pdescription,
            price=pprice
        )
        
        # Save the product instance first to get its primary key
        product.save()

        # Now associate uploaded images with the product
        for idx, image_file in enumerate(uploaded_images, start=1):
            setattr(product, f'property_image{idx}', image_file)

        product.save()
        return redirect('/seller_dashboard')  # Save again after adding images

    return render(request, 'addpdt.html')

#seller update funtion
def update_pdt(request, pid):
    product = product_tbl.objects.get(id=pid)

    if request.method == 'POST':
        pname = request.POST.get('name')
        ptype = request.POST.get('type')
        pdimension = request.POST.get('pdimen')
        pprice = request.POST.get('price')
        paddress = request.POST.get('add')
        posses = request.POST.get('poss')
        pdescription = request.POST.get('description')

        # Get a list of uploaded images
        uploaded_images = []
        for i in range(1, 9):  # Assuming image fields are named image1, image2, ..., image8
            image_key = f'image{i}'
            if image_key in request.FILES:
                uploaded_images.append(request.FILES.get(image_key))

        # Update product instance with new data
        product.property_name = pname
        product.property_type = ptype
        product.dimension = pdimension
        product.price = pprice
        product.address = paddress
        product.possession = posses
        product.description = pdescription

        # Save the product instance first to get its primary key
        product.save()

        # Now associate uploaded images with the product
        for idx, image_file in enumerate(uploaded_images, start=1):
            setattr(product, f'property_image{idx}', image_file)

        product.save()  # Save again after adding images
        return redirect('/seller_dashboard')  # Redirect to the seller dashboard

    return render(request, 'updatepdt.html', {'product': product})
    
def pdt_delete(request,pid):
    product = get_object_or_404(product_tbl, id=pid)
    product.delete()

    # if request.method == 'POST':
    #     # Delete the product
    #     product.delete()
    #     return redirect('/seller_dashboard')

    return redirect('/seller_dashboard')
