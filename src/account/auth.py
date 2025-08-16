from django.contrib.auth.backends import ModelBackend

from account.models import User


class ModelBackendWithEmail(ModelBackend):
    """
    An auth backend with phone number and password
    """

    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
