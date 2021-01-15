from django.db import models

class contact_details(models.Model):
    contact_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    email=models.EmailField(max_length=30)
    

    def __str__(self):
        return self.contact_name


    class Meta:
        db_table="contact_details"
         