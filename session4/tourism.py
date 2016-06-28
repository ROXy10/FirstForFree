from django.db import models

class Hotel(models.Model):

	name = models.CharField(verbose_name="Name",max_length=256,	blank=True,	default='',	)

    city = models.ForeignKey("City",verbose_name="City",blank=True,	)

	country = models.ForeignKey("Country",	verbose_name="Country",	blank=True,	)

	email = models.EmailField(verbose_name="Email",	max_length=256,	blank=True,	default='',	)

	phone = models.CharField(verbose_name="Phone",	max_length=256,	blank=True,	default='',	)
    
    rating = models.IntegerField(verbose_name="Rating",	blank=True,	default=1,	)

	description = models.TextField(	verbose_name="Description",	max_length=3000,blank=True,	default='',	)
    
    class Meta(object):
		verbose_name = "Hotel"
		verbose_name_plural = "Hotels"
	
    def __unicode__(self):
		return "%s - %s(%s)" % (self.name, self.city.name, self.country.name)

class Country(models.Model):

	name = models.CharField(verbose_name="Name",max_length=256,	blank=True,	default='',	)
	
    class Meta(object):
		verbose_name = "Country"
		verbose_name_plural = "Countries"
	
    def __unicode__(self):
		return self.name


class Client(models.Model):


	first_name = models.CharField(verbose_name="First name",max_length=256,blank=True,default='',)

	last_name = models.CharField(verbose_name="Last name",max_length=256,blank=True,default='',)


	country = models.ForeignKey("Country",verbose_name="Country",blank=True,)

	city = models.ForeignKey("City",verbose_name="City",blank=True,	)

	subscribe = models.BooleanField(verbose_name="Subscribe",blank=True,)

    class Meta(object):
		verbose_name = "Client"
		verbose_name_plural = "Clients"
        
	def __unicode__(self):
		return u"%s %s - %s(%s)" % (self.first_name, self.last_name, 
								   self.city.name, self.country.name)

                                   
class City(models.Model):

	name = models.CharField(verbose_name="Name",max_length=256,	blank=True,	default='',	)

	country = models.ForeignKey("Country",verbose_name="Country",blank=True,)

    
	class Meta(object):
		verbose_name = "City"
		verbose_name_plural = "Cities"
        
	def __unicode__(self):
		return u"%s - %s" % (self.name, self.country.name)
        
class Email(models.Model):

	email = models.EmailField(verbose_name="E-mail",max_length=256,	blank=True,	default='',	)

	client = models.ForeignKey(	"Client",verbose_name="Client",blank=True,)

    
	class Meta(object):
		verbose_name = "E-mail"
		verbose_name_plural = "E-mails"
        
	def __unicode__(self):
		return u'%s %s - %s' % (self.client.first_name,
								self.client.last_name,
								self.email)

class Phone(models.Model):

	phone = models.CharField(verbose_name="Phone",max_length=256,blank=True,default='',)

	client = models.ForeignKey("Client",verbose_name="Client",blank=True,)

    class Meta(object):
		verbose_name = "Phone"
		verbose_name_plural = "Phones"
        
	def __unicode__(self):
		return u'%s %s - %s' % (self.client.first_name,self.client.last_name,self.phone)


class Tour(models.Model):

	name = models.CharField(verbose_name="Name",max_length=256,blank=True,default='',)

	hotel = models.ForeignKey("Hotel",verbose_name="Hotel",	blank=True,	)

	start_date = models.DateField(verbose_name="Start date",blank=True,	)

	end_date = models.DateField(verbose_name="End date",blank=True,	)

	price = models.DecimalField(verbose_name="Price",blank=True,default=0.0,decimal_places=2, max_digits=5)

	available_places = models.IntegerField(verbose_name="Available places",	blank=True,	default=0,)

	description = models.TextField(verbose_name="Description",max_length=3000,blank=True,default='',)

    class Meta(object):
		verbose_name = "Tour"
		verbose_name_plural = "Tours"
        
	def __unicode__(self):
		return '%s - %d/%d' % (self.name, self.available_places, self.total_places)

class OrderStatus(models.Model):

	status = models.CharField(verbose_name="Status",max_length=256,blank=True,default='',)

    class Meta(object):
		verbose_name = "Order status"
		verbose_name_plural = "Order statuses"
        
	def __unicode__(self):
		return self.status

class Order(models.Model):

	client = models.ForeignKey("Client",verbose_name="Client",blank=True,)

	tour = models.ForeignKey("Tour",verbose_name="Tour",blank=True,	)

	places = models.IntegerField(verbose_name="Places",blank=True,	default=0,)

	paid = models.DecimalField(	verbose_name="Paid",blank=True,default=0.0,	decimal_places=2, max_digits=5)

	order_status = models.ForeignKey("OrderStatus",verbose_name="Order status",	blank=True,)

	def __unicode__(self):
		return "%s %s - %s %s" % (self.client.first_name, self.client.last_name, 
								  self.tour.name, self.order_status.status)