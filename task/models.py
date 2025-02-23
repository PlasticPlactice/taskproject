from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', '低'),
        ('medium', '中'),
        ('high', '高'),
    ]

    STATUS_CHOICES = [
        ('incomplete', '未完了'),
        ('complete', '完了'),
    ]

    title = models.CharField(max_length=255)
    last_day = models.DateField()
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='incomplete',
    )  

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['last_day']
