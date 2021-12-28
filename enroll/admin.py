from django.contrib import admin
from .models import (Profile, Account, Bank, Card,Transaction,
  PaymentMethod ,Pan_card , Adhar_card)

admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Bank)
admin.site.register(Card)
admin.site.register(Adhar_card)
admin.site.register(Pan_card)
admin.site.register(PaymentMethod)
admin.site.register(Transaction)