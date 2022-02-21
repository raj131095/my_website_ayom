from django.contrib import admin
from .models import User,Create_Shop,UploadedImage,Watchlist,Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Create_Shop)
admin.site.register(UploadedImage)
admin.site.register(Watchlist)
admin.site.register(Comment)