from django.db import models

class Student(models.Model):

    GENDERS = (
        ("F","female"),
        ("M","male"),
        ("U","undiscussed")
    )

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique= True)
    email = models.EmailField(max_length= 100)
    gender = models.CharField(max_length=1, choices = GENDERS)
    percentage = models.FloatField()

    insttiute = models.ForeignKey("Institute", on_delete= models.CASCADE, null = True,blank =True)

    def __str__(self):
        return self.name

class Institute(models.Model):

    TYPES =(
        ("C","College"),
        ("H","Heighschool")
    )

    name = models.CharField(max_length=200)
    type_of_instiute = models.CharField(max_length=1, choices= TYPES )

    def __str__(self):
        return self.name
