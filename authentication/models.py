
from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
	username = models.CharField(
		max_length=150,
		unique=True,

    # optional: you can uncomment the validators if you want to enforce specific username rules
		# validators=[
		# 	RegexValidator(
		# 		regex=r"^[\w.@+\- ]+$",
		# 		message="Username may contain letters, numbers, spaces, and @/./+/-/_ characters.",
		# 	)
		# ],
		error_messages={"unique": "A user with that username already exists."},
	)
	phone_number = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.username
