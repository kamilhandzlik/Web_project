from django.db import models

# Create your models here.
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1  # Ensure the primary key is always 1
        if self.__class__.objects.exists() and not self.pk:
            self.pk = self.__class__.objects.first().pk
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Prevent deletion of singleton instance

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
class ContactForm(SingletonModel):
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    house_number = models.CharField(max_length=50, null=True)
    email_address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    working_days = models.CharField(max_length=50, null=True)
    working_hours = models.CharField(max_length=50, null=True)
    vat_number = models.CharField(max_length=50, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)

class MainPage(SingletonModel):
    title = models.CharField(max_length=50)
    description_1_subtitle = models.TextField(default="Wstaw tytół pod pierwszy akapit")
    description_1 = models.TextField(default="Wstaw swój tekst.")
    description_2_subtitle = models.TextField(default="", blank=True)
    description_2 = models.TextField(default="", blank=True)
    description_3_subtitle = models.TextField(default="", blank=True)
    description_3 = models.TextField(default="", blank=True)
    description_4_subtitle = models.TextField(default="", blank=True)
    description_4 = models.TextField(default="", blank=True)
    description_5_subtitle = models.TextField(default="", blank=True)
    description_5 = models.TextField(default="", blank=True)