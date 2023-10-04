from django.db import models




class RegForm(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=20)
    materials_provide = models.CharField(max_length=20)

    def __str__(self):
        return self.name