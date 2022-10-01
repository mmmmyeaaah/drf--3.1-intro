from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=60, null=False, verbose_name='Имя датчика')
    description = models.CharField(max_length=60, null=False, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(null=False, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'