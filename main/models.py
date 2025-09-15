import uuid
from django.db import models

# Create your models here.

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('home_jersey', 'Home jersey'),
        ('away_jersey', 'Away jersey'),
        ('third_jersey', 'Third jersey'),
        ('goalkeeper_jersey', 'Goalkeeper jersey'),
        ('thrift_jersey', 'Thrift jersey'),
        ('special_jersey', 'Special jersey'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='home_jersey')
    is_featured = models.BooleanField()

    def __str__(self):
        return self.name
    
    
