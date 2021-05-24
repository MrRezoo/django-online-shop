from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, full_name, phone_number):
        if not email:
            raise ValueError('users must have email')
        if not full_name:
            raise ValueError('users must have full Name')
        if not phone_number:
            raise ValueError('users must have full Name')

        user = self.model(email=self.normalize_email(email), full_name=full_name, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password, phone_number):
        user = self.create_user(email, full_name, password, phone_number)
        user.is_admin = True
        user.save(using=self)
        return user
