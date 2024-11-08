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

