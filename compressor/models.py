import random
import string
import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class ImageCompressor(models.Model):
    image_name = models.CharField(max_length=225, default=''.join(random.choice(string.ascii_letters) for i in range(10)) )
    image_file = models.ImageField(upload_to='image-compressed')

    def save(self, *args, **kwargs):
        if not self.id:
            self.image_file = self.compressImage(self.image_file)
        super(ImageCompressor, self).save(*args, **kwargs)

    def compressImage(self,image_file):
        imageTemproary = Image.open(image_file)
        image_file_name = image_file.name
        image_type = image_file_name.split('.')[-1]
        
        if image_type == 'png':
            imageTemproary_converted = imageTemproary.convert('P', palette=Image.ADAPTIVE)
            outputIoStream = BytesIO()
            imageTemproary_converted.save(outputIoStream , format='png', quality=80, optimize=True)
            outputIoStream.seek(0)
            image_file = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.png" % image_file.name.split('.')[0], 'image/png', sys.getsizeof(outputIoStream), None)
        elif image_type == 'jpg' or 'jpeg':
            rgb_imageTemproary = imageTemproary.convert('RGB')
            outputIoStream = BytesIO()
            rgb_imageTemproary.save(outputIoStream , format='JPEG', quality=60, optimize=True)
            outputIoStream.seek(0)
            image_file = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image_file.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)

        return image_file

    def __str__(self):
        return self.image_name