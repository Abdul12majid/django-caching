from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	serial_number = models.UUIDField(default=uuid.uuid4, editable=False)
	
	def __str__(self):
		return self.name + ' ' + str(self.serial_number)