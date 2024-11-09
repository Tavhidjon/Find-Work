from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    register_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/images",null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
    
    

    
    
class Talant(models.Model):
    title = models.CharField( max_length=50)
    description  = models.TextField()
    image =  models.ImageField(upload_to="static/images",null=True,blank=True)
    video  = models.FileField(upload_to="static/images",null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField()
    create_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
    



    
class Aplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talant = models.ForeignKey(Talant,  on_delete=models.CASCADE)
    price = models.IntegerField()
    message = models.CharField(max_length=50,null=True)
    duraction = models.TextField()
    create_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.name