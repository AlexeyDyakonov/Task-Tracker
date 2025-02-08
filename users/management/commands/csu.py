from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания админа"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="alexey",
        )
        user.set_password("4451")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
