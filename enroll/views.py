
from django.shortcuts import redirect, render

from .forms import (RegistrationFormUser ,
ImageForm ,PanImageForm  ,ProfileForm , TransactionForm)

from django.contrib import messages

from .models import (Profile, Account, Bank, 

Card, Adhar_card,Pan_card, PaymentMethod , Transaction)


from django.views import View

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def email_user(request):
  send_mail(
    'django test email', 
    'success recieve email', 
    'kasimsaifi8826@gmail.com',
    ['kasim@veeaargroup.com'],
    fail_silently=False
  )



class home(View):
    def get(self, request):
      return render(request , 'home.html')

class  Registration_User_Form(View):
    def get(self , request):
      form=RegistrationFormUser()
      return render(request , 'registration.html',{'form':form})

    def post(self , request):
        form=RegistrationFormUser(request.POST or None)
        if form.is_valid():
            #messages.info(request, "Registration is Successfully!!")
            form.save()
            return redirect('/')
        return render(request, 'registration.html' , {'form':form})    



class Adhar_card_profile(View):
  def get(self , request):
    form=ImageForm()
    return render(request , 'adhar.html')

  @method_decorator(login_required)
  def post(self , request):
    form= ImageForm(request.POST or None , request.FILES) 
    if form.is_valid():
            form.save()
            messages.info(request, "Please pan card Upload")
            return redirect('/pan/')
    img=Adhar_card.objects.all() 
    return render(request, 'adhar.html',{'img':img ,'fm':form ,'name':request.user})       

        


class Pan_card_profile(View):
  def get(self , request):
    form=PanImageForm()
    return render(request , 'pan.html')
    
  @method_decorator(login_required)
  def post(self , request):
    form= PanImageForm(request.POST or None , request.FILES) 
    if form.is_valid():
            form.save()
            messages.info(request, "Welcome")
            return redirect('/')
    img=Pan_card.objects.all() 
    return render(request, 'pan.html',{'img':img ,'fm':form , 'name':request.user })       


def business(request):
  return render(request, 'business.html')


class User_Profile(View):
    def get(self,request):
      form=ProfileForm()
      stu=Profile.objects.all()  
      return render(request , 'profile.html' , {'stu':stu,'form':form})
    
    @method_decorator(login_required)
    def post(self , request):
      form=ProfileForm(request.POST or None )
      if form.is_valid():
        messages.info(request , "Profile Create Successfullly!!")
        form.save()
      stu=Profile.objects.all()  
      return render(request, 'profile.html',{ 'form':form ,'stu':stu})  
          
class Update_user_profile(View ):
  def get(self , request , id):
      pi=Profile.objects.get(pk=id)
      form=ProfileForm(instance=pi)
      return render(request , 'profile_edit.html',{'form':form})
  
  @method_decorator(login_required)
  def post(self , request , id):
    pi=Profile.objects.get(pk=id)
    form=ProfileForm(request.POST or None , instance=pi) 
    if form.is_valid():
      messages.info(request , "Update Successfylly!!")
      form.save()
      return redirect('/profile/')
    return render(request , 'profile_edit.html')     
     
class Transaction_User_Form(View):
  def get(self , request):
    form=TransactionForm()
    history=Transaction.objects.all()
    return render(request , 'transaction.html' ,{'form':form, 'history':history})

  @method_decorator(login_required)
  def post(self , request):
    form=TransactionForm(request.POST or None )
    if form.is_valid():
      TP=form.cleaned_data['transaction_type']
      TC=form.cleaned_data['category']
      TA=form.cleaned_data['amount']
      user=Transaction(transaction_type=TP , category=TC , amount=TA)
      user.save()
      messages.info(request, 'Success!')
      form=TransactionForm()
    history=Transaction.objects.all()

    return render(request , 'transaction.html',{'form':form, 'history':history})  




# def ImageUploaderProject(request):
#       if request.method=='POST':
#         fm=ImageForm(request.POST, request.FILES)
#         if fm.is_valid():
#          fm.save()
#          messages.info(request, 'Image Successfully Upload!!')
#          return redirect('/adhar/')
#       fm=ImageForm() 
#       img = Adhar_card.objects.all()   
#       return render(request, 'adhar.html',{'img':img ,'fm':fm, 'name':request.user })
  