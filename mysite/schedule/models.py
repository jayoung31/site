from django.db import models

class Schedule(models.Model):
    title = models.CharField(max_length=100)  # 수행평가 제목
    date = models.DateField()  # 수행평가 날짜

    def __str__(self):
        return f"{self.date} - {self.title}"
