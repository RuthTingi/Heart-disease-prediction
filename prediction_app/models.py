from django.db import models

class PatientRecord(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    glucose = models.FloatField()
    sysBP = models.FloatField()
    diaBP = models.FloatField()
    BMI = models.FloatField()
    smoker = models.BooleanField()
    prediction = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.prediction}"
