from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.html import format_html

STATE_CHOICES=(
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Utter Pradesh','Utter Pradesh'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & kasmir','Jammu & kasmir'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    first_name=models.CharField(max_length=90)
    last_name=models.CharField(max_length=90)
    birthday = models.DateField(default=None)
    city=models.CharField(max_length=90)
    state=models.CharField(max_length=90 , choices=STATE_CHOICES)
    address=models.CharField(max_length=250, default=None)

    
    def __str__(self):
        return str(self.id)



class Adhar_card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True)
    forent_photo=models.ImageField(upload_to='forent_adhar_image')
    back_photo=models.ImageField(upload_to='back_adhar_image')
    
    def __str__(self):
        return str(self.id)
    

class Pan_card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE  ,null=True, blank=True)
    forent_pan_image=models.ImageField(upload_to='pan_image')

    def __str__(self):
        return str(self.id)



class PaymentMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    method_type = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, related_name='payment_user', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.method_id)


class Account(models.Model):
    payment = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.00)




class Bank(models.Model):
    payment = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)
    owner_first_name = models.CharField(max_length=255, default=None)
    owner_last_name = models.CharField(max_length=255, default=None)
    ifsc_code = models.CharField(max_length=255, default=None)
    account_number = models.CharField(max_length=16, default=None)
    confirm_account_number = models.CharField(max_length=16, default=None)

  
  
Card_Type = (
    ('Credit', 'Credit Card'),
    ('Debit', 'Debit Card'),
)


class Card(models.Model):
    payment = models.OneToOneField(PaymentMethod, on_delete=models.DO_NOTHING)
    card_type = models.CharField(max_length=45, choices=Card_Type)
    card_number = models.CharField(max_length=16, default=None)
    owner_first_name = models.CharField(max_length=45)
    owner_last_name = models.CharField(max_length=45)
    cvv = models.CharField(max_length=3, default=None)
    expires = models.DateField(default=None)



 

Transaction_Type = (
    ('send', 'Send'),
    ('request', 'Request'),
    ('transfer', 'Transfer'),
)


Categories = (
    ('Bank', 'Bank Transfer'),
    ('Utilities', 'Bills & Utilities'),
    ('Transportation', 'Auto & Transport'),
    ('Groceries', 'Groceries'),
    ('Food', 'Food'),
    ('Shopping', 'Shopping'),
    ('Health', 'Healthcare'),
    ('Education', 'Education'),
    ('Travel', 'Travel'),
    ('Housing', 'Housing'),
    ('Entertainment', 'Entertainment'),
    ('Others', 'Others'),
)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True ,blank=True )
    transaction_type = models.CharField(max_length=45, choices=Transaction_Type, default='')
    category = models.CharField(max_length=45, choices=Categories)
    amount = models.FloatField(default=0.00)
    def __str__(self):
        return str(self.transaction_id)
    