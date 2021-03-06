from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(default = 'name',max_length = 200)
    bio = models.CharField(default = 'bio', max_length = 300)
    location = models.CharField(default = 'location' , max_length = 100)
    user_website = models.URLField(blank = True ,null=True)
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self ,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
   
