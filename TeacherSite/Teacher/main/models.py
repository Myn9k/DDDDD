from django.db import models


class Diploms_model(models.Model):
    name = models.CharField('Название диплома', max_length=255, null=True, blank=True)
    text = models.CharField('Текст к диплому', max_length=255, blank=True)
    picture = models.ImageField('Фотография', blank=False, null=True, upload_to='img/')

    class Meta:
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return f"""{self.name}"""


class Cards_model(models.Model):
    name = models.CharField('Название карточки', max_length=255, null=True, blank=True)
    picture = models.ImageField('Фотография', blank=False, null=True, upload_to='img/')
    link = models.CharField('Ссылка', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f"""{self.name}"""


class VieoGalery_model(models.Model):
    name = models.CharField('Название видео', max_length=255, null=True, blank=True)
    text = models.CharField('Текст к видео', max_length=255, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='img/')

    class Meta:
        verbose_name = 'Видеогалерея'
        verbose_name_plural = 'Видеогалерея'

    def __str__(self):
        return f"""{self.name}"""

class PhotoGalery_model(models.Model):
    name = models.CharField('Название фото', max_length=255, null=True, blank=True)
    text = models.CharField('Текст к фотографии', max_length=255, blank=True)
    picture = models.ImageField('Фотография', blank=False, null=True, upload_to='img/')

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалерея'

    def __str__(self):
        return f"""{self.name}"""

class Dostijenia_model(models.Model):
    name = models.CharField('Название достижения', max_length=255, null=True, blank=True)
    Year = models.CharField('Какой год', max_length=255, blank=True)
    picture = models.ImageField('Фотография', blank=False, null=True, upload_to='img/')


    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return f"""{self.name}"""


class DostijeniaSchoolboy_model(models.Model):
    name = models.CharField('Название достижения', max_length=255, null=True, blank=True)
    Year = models.CharField('Какой год', max_length=255, blank=True)
    picture = models.ImageField('Фотография', blank=False, null=True, upload_to='img/')


    class Meta:
        verbose_name = 'Достижения учащихся'
        verbose_name_plural = 'Достижения учащихся'

    def __str__(self):
        return f"""{self.name}"""