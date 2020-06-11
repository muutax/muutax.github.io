from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Records(models.Model):
    create_date = models.DateTimeField(auto_now = True)
    second_name = models.CharField(max_length = 15, verbose_name = "Фамилия")
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество")
    date_of_birth = models.CharField(max_length=10  , verbose_name="Дата рождения")
    the_class = models.CharField(max_length=2, verbose_name="Класс")
    educational_institution = models.CharField(max_length=50, verbose_name="Учеб.учреждение")
    place_of_study = models.CharField(max_length=15, verbose_name="Место обучения")
    country = models.CharField(max_length=10, verbose_name="Страна")
    region = models.CharField(max_length=17, verbose_name="Регион")
    e_mail = models.CharField(max_length=20, verbose_name="Email")
    phone_number = models.CharField(max_length=11, verbose_name="Телефон")
    events = models.CharField(max_length=200, verbose_name="Мероприятия")

    def __str__(self):
        return '%s %s-%s' % (self.first_name, self.second_name, self.patronymic)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "Записи"