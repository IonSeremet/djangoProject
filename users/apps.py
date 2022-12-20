from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def readu(self):
        import users.signals
