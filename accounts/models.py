from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class BusinessProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	nom = models.CharField("Nom de l'entreprise", max_length=200)
	presentation = models.TextField("Présentation de l'entreprise", max_length=500, blank=True)
	logo = models.ImageField("Image", upload_to='logos/', blank=True,
null=True, max_length=255)

	pays = models.CharField("Pays", max_length=100, blank=True)
	province = models.CharField("Province", max_length=100, blank=True)
	ville = models.CharField("Ville", max_length=100, blank=True)
	commune = models.CharField("Commune", max_length=100, blank=True)
	adresse = models.TextField(max_length=500, blank=True)
	telephone = models.CharField(max_length=100, blank=True)


	email = models.EmailField("E-mail", max_length=200, blank=True)
	website = models.URLField("Site Web", max_length=200, blank=True)
	certifications = models.CharField(max_length=200, blank=True)
	annee_existence = models.CharField("Année de création",max_length=100, blank=True)
	annee_experience = models.CharField(max_length=100, blank=True)
	travaux_realises = models.CharField(max_length=300, blank=True)

	business_partners = models.CharField(max_length=200, blank=True)
	business_references = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_business_profile(sender, instance, created, **kwargs):
	if created:
		BusinessProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_business_profile(sender, instance, **kwargs):
	instance.businessprofile.save()
