from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Question(models.Model):
	title = models.TextField(null=True, blank=True)
	status = models.CharField(default='inactive', max_length=10)
	created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Choice(models.Model):
	question = models.ForeignKey('Question',on_delete=models.CASCADE)
	text = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	designation = models.CharField(max_length=20, null=False, blank= False)
	salary = models.IntegerField(null=True, blank=True)


	class Meta:
		ordering = ('-salary',)

	def __str__(self):
		return"{0}{1}".format(self.user)

@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(User=instance)
	else:
		instance.Profile.save()

