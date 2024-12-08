from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Костыль для хэширования пароля у пользователей'

    def handle(self, *args, **kwargs):
        USER = get_user_model()
        users = USER.objects.all()
        for u in users:
            if len(u.password) < 88:
                u.set_password(u.password)
                u.save()
