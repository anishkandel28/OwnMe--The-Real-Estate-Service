from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user   
    
     
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=True,
                                  verbose_name=_("Firstname"))
    last_name = models.CharField(max_length=255, null=True,
                                 verbose_name=_("Lastname"))
    username = None
    phone = models.CharField(max_length=20, null=True,
                             verbose_name=_("Phone"))
    address = models.ForeignKey('core.Address', null=True, blank=True,
                                on_delete=models.DO_NOTHING,
                                verbose_name=_("Address"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def get_groups(self):
        return [group.name for group in self.groups.all()]
    get_groups.short_description = _("Groups")



        
        
