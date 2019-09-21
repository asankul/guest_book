from django.db import models

STATUS_CHOICES = [('active', 'Активная'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    date_of_creation = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    date_of_edition = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования')
    status = models.CharField(choices=STATUS_CHOICES, max_length=200, default='active')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)
