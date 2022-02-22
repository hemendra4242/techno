from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=100)
    Image1 = models.FileField(null=True)
    Image2 = models.FileField(null=True)
    Image3 = models.FileField(null=True)
    Image4 = models.FileField(null=True)
    Image5 = models.FileField(null=True)
    Before_price = models.FloatField()
    After_price = models.FloatField()
    discount = models.IntegerField()
    Choices = (
        ('Smart Phone', 'Smart Phone'),
        ('Camera', 'Camera'),
        ('Games', 'Games'),
        ('Smart Speakers', 'Smart Speakers'),
        ('Smart Watch', 'Smart Watch'),
        ('Tablets', 'Tablets'),
        ('Laptops', 'Laptops'),
        ('Mouse', 'Mouse'),
        ('keyboard', 'Keyboard'),
        ('Headphone', 'Headphone'),
        ('Monitors', 'Monitors'),
        ('TV', 'TV')
    )
    choice = models.CharField(max_length=100, choices=Choices, default=None)
    Description1title = models.CharField(max_length=100)
    Description2title = models.CharField(max_length=100)
    Description3title = models.CharField(max_length=100)
    Description4title = models.CharField(max_length=100)
    Description1 = models.TextField()
    Description2 = models.TextField()
    Description3 = models.TextField()
    Description4 = models.TextField()
    Buy_link = models.URLField()
    Dateofpublished = models.DateTimeField(auto_now_add=True)
    Brand = models.CharField(max_length=100)
    Memory = models.CharField(max_length=200, blank=True, default=None)
    cchoice = (
        ('Red', 'Red'),
        ('White', 'White'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Pink', 'Pink'),
        ('Green', 'Green'),
        ('Sky Blue', 'Sky Blue'),
        ('Yellow', 'Yellow'),
        ('Black', 'Black')
    )
    Colour = models.CharField(max_length=50, choices=cchoice, default=None)
    Memory = models.CharField(max_length=200, blank=True, default=None)
    cellular_technology = models.CharField(max_length=200, blank=True, default=None)
    Included_items = models.CharField(max_length=200, blank=True, default=None)
    Model = models.CharField(max_length=200, blank=True, default=None)
    Camera_quality = models.CharField(max_length=200, blank=True, default=None)
    Model = models.CharField(max_length=200, blank=True, default=None)
    screensize = models.CharField(max_length=200, blank=True, default=None)
    RAM = models.CharField(max_length=200, blank=True, default=None)
    ROM = models.CharField(max_length=200, blank=True, default=None)
    Resolution = models.CharField(max_length=200, blank=True, default=None)
    Zoom = models.CharField(max_length=200, blank=True, default=None)
    displaytype = models.CharField(max_length=200, blank=True, default=None)
    Genre = models.CharField(max_length=200, blank=True, default=None)
    Mode = models.CharField(max_length=200, blank=True, default=None)
    releasedate = models.DateTimeField(auto_now_add=True)
    Bluetoothconnectivity = models.CharField(max_length=200, blank=True, default=None)
    waterresistance = models.CharField(max_length=200, blank=True, default=None)
    connectivitytype = models.CharField(max_length=200, blank=True, default=None)
    storage = models.CharField(max_length=200, blank=True, default=None)
    Zoom = models.CharField(max_length=200, blank=True, default=None)
    Graphicscoprocessor = models.CharField(max_length=200, blank=True, default=None)
    Batterylife = models.CharField(max_length=200, blank=True, default=None)
    compatibledevices = models.CharField(max_length=200, blank=True, default=None)
    Refreshrate = models.CharField(max_length=200, blank=True, default=None)
    Supportedinternetservices = models.CharField(max_length=200, blank=True, default=None)
    Specialfeatures = models.CharField(max_length=200, blank=True, default=None)
    series = models.CharField(max_length=200, blank=True, default=None)
    def get_absolute_url(self):
        return reverse('product', kwargs={'name':self.Title})

    class Meta:
        verbose_name = 'Product'
        get_latest_by = ['-Dateofpublished']

class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=300)



