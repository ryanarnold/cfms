from djang.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_plural_name = 'Categories'

	def __str__(self):
		return self.name

class Platform(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Office(models.Model):
	name = models.CharField(max_length=100)
	parent = models.ForeignKey(Office, null=True)

	def __str__(self):
		return self.name

class Complaint(models.Model):
	number = models.CharField(max_length=13)
	message = models.CharField(max_length=10000)
	date_received = models.DateTimeField(auto_now=True)
	office_referred = models.ForeignKey(Office)
	sender_name = models.CharField(max_length=100)
	sender_email = models.EmailField(null=True)
	sender_contact = models.CharField(max_length=100, null=True)
	sender_company = models.CharField(max_length=100, null=True)
	action_taken = models.CharField(max_length=10000, null=True)
	date_action = models.DateTimeField(null=True)
	remarks = models.CharField(max_length=5000)
	category = models.ForeignKey(Category)
	platform = models.ForeignKey(Platform)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.number