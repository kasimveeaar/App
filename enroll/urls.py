from django.urls import path,include
from enroll.views import(
home,Registration_User_Form,email_user , business
,Adhar_card_profile ,Pan_card_profile,
Update_user_profile, User_Profile,
Transaction_User_Form
 )

from django.contrib.auth import views as auth_views

from enroll.forms import (
     LoginuserForm,
      MypasswordchangeForm,
      Email_Check,
      Usersetpasswordform
)

urlpatterns = [
    path('' , home.as_view() , name='home'),
    path('business/' , business , name='business'),
    path('<int:id>',Update_user_profile.as_view(), name='updatedata'),
    path('profile/',User_Profile.as_view()  , name='profile'),
    # path('img/' , ImageUploaderProject , name='img'),
    path('adhar/' , Adhar_card_profile.as_view() , name='adhar'),
    path('pan/' , Pan_card_profile.as_view() , name='pan'),
    path('transaction/',Transaction_User_Form.as_view(), name='transaction'),



    path('sign/', Registration_User_Form.as_view() , name='sign'),
    path('accounts/login/' , auth_views.LoginView.as_view(template_name='login.html' ,
     authentication_form=LoginuserForm) , name='login'),
    path('logout/' , auth_views.LogoutView.as_view(next_page='login') , name='logout'),
    path('changepassword/' , auth_views.PasswordChangeView.
    as_view(template_name='passwordchange.html',
    form_class=MypasswordchangeForm , success_url='/passwordchangedone/'),name="changepassword") ,
    path('passwordchangedone/'
    ,auth_views.PasswordChangeView.as_view(template_name=
    'passwordchangedone.html' ),name="passwordchangedone"),

    path('password_reset/' , auth_views.PasswordResetView.as_view(
    template_name='password_reset.html' , 
    form_class=Email_Check),name='password_reset'),

    path('password_reset/done' , auth_views.PasswordResetDoneView.as_view(
    template_name='password_reset_done.html'),name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/' ,
    auth_views.PasswordResetConfirmView.as_view(
    template_name='password_reset_confirm.html' , 
    form_class=Usersetpasswordform),name='password_reset_confirm'),

    path('password_reset_complete/' , auth_views.PasswordResetCompleteView.as_view(
    template_name='password_complete.html'),name='password_reset_complete'),
    path('email/' , email_user  , name="email")


]