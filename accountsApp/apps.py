from django.apps import AppConfig


class AccountsappConfig(AppConfig):
    name = 'accountsApp'

    def ready(self):
        import accountsApp.signals