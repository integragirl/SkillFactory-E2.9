from django.db import models
from django.utils import timezone
from django.core.mail import send_mail

import threading
import uuid
import time
from django.utils.translation import gettext as _


class MailPost(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name=_("Уникальный ключ"))
    text = models.TextField(verbose_name='Текст')
    timeSecond = models.IntegerField(blank=True, null=True, verbose_name='Кол-во секунд')
    sent = models.BooleanField(default=False, verbose_name='Отправлено (да/нет)')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.sent == False:
            threads = []
            t = threading.Thread(target=worker, args=(self, ))
            threads.append(t)
            t.start()
            t.join()


def worker(self):
    time.sleep(self.timeSecond)
    answ = send_mail('Django mail', self.text, 'integragirl@mail.ru', ['integragirl@mail.ru'], fail_silently=False)
    if answ == 1:
        self.sent = True
        self.save()
