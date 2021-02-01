from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=64)
	body = models.CharField(max_length=128, null=True)

	def __str__(self):
		return self.name
		
class Subcategory(models.Model):
	name = models.CharField(max_length=64)
	body = models.CharField(max_length=128, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=1024, null=True)
	subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
	price = models.FloatField(default=0)

	def __str__(self):
		return self.name

