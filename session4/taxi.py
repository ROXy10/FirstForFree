from django.db import models

class Client(models.Model):

	class Meta(object):
		verbose_name = "Client"
		verbose_name_plural = "Clients"

	first_name = models.CharField(verbose_name="First name",max_length=256,blank=True,default='',)

	middle_name = models.CharField(verbose_name="Middle name",max_length=256,blank=True,default='',	)

	phone = models.CharField(verbose_name="Phone",max_length=256,blank=True,default='',)

	last_order = models.DateField(verbose_name="Last order",blank=True,)

	def __unicode__(self):
		return u"%s - %s" % (self.first_name, self.phone)

class Car(models.Model):

	model = models.ForeignKey("Model",verbose_name="Model",blank=True)

	number = models.CharField(verbose_name="Number",max_length=256,blank=True,default='',)

	color = models.ForeignKey("Color",verbose_name="Color",blank=True)
    
    class Meta(object):
		verbose_name = "Car"
		verbose_name_plural = "Cars"

	def __unicode__(self):
		return u"%s - %s - %s" % (self.model.name, self.number, self.color.name)

class Driver(models.Model):

	first_name = models.CharField(verbose_name="First name",max_length=256,blank=True,default='',)

	last_name = models.CharField(verbose_name="Last name",max_length=256,blank=True,default='',)

	phone = models.CharField(verbose_name="Phone",max_length=256,blank=True,default='',)

	car = models.ForeignKey("Car",verbose_name="Car",blank=True)

	ready = models.BooleanField(verbose_name="Ready",blank=True)
    
	class Meta(object):
		verbose_name = "Driver"
		verbose_name_plural = "Drivers"

	def __unicode__(self):
		return u"%s - %s - %s - %s" % (self.first_name, self.last_name, self.car.model.name, self.phone)

class Order(models.Model):

	class Meta(object):
		verbose_name = "Order"
		verbose_name_plural = "Orders"

	client = models.ForeignKey(	"Client",verbose_name="Client",blank=True)

	driver = models.ForeignKey("Driver",verbose_name="Driver",blank=True)

	price = models.DecimalField(verbose_name="Price",blank=True,default=0.0,decimal_places=2, max_digits=5)

	discount = models.DecimalField(verbose_name="Discount",blank=True,default=0.0,decimal_places=2, max_digits=5)

	total_price = models.DecimalField(verbose_name="Total price",blank=True,default=0.0,decimal_places=2, max_digits=5)

	place = models.CharField(verbose_name="Place",max_length=256,blank=True,default='')

	date_time = models.DateTimeField(verbose_name="Date&Time",blank=True,)

	order_status = models.ForeignKey("OrderStatus",verbose_name="Order status",blank=True,)

	def __unicode__(self):
		return u"%s - %s - %s" % (self.price, self.place, self.date_time, self.order_status.name)

class OrderStatus(models.Model):

	status = models.CharField(verbose_name="Status",max_length=256,blank=True,default='',)
    
    class Meta(object):
		verbose_name = "Order status"
		verbose_name_plural = "Order statuses"

	def __unicode__(self):
		return self.status