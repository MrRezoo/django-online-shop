from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password):
        if not email:
            raise ValueError('users must have Email')
        if not full_name:
            raise ValueError('users must have Full Name')

        user = self.model(email=self.normalize_email(email), phone_number=phone_number, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, password):
        user = self.create_user(email, full_name, phone_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
