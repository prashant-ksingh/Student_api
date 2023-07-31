from rest_framework import serializers
from api import models

class InstituteSerializers(serializers.ModelSerializer):
    model = models.Institute
    fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):

    institute = InstituteSerializers(read_only = True)

    class Meta:
        model = models.Student
        fields = "__all__"