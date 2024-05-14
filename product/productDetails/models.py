from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class superAdmin(models.Model):
    superAdminName = models.CharField(max_length=50)
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class admin(models.Model):
    adminName = models.CharField(max_length=50)
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    superAdmin = models.ForeignKey(superAdmin, on_delete=models.CASCADE)

class user(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    userName = models.CharField(max_length=50)
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    admin = models.ForeignKey(admin, on_delete=models.CASCADE)
    
class product(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    productName = models.CharField(max_length=50)
    productDescription = models.TextField()
    productCreatedDate = models.DateTimeField(auto_now_add=True)
    productUpdatedDate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
