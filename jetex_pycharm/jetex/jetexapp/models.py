from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    password = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.user_name

class Contactus(models.Model):
     
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    subject = models.CharField(max_length = 200, null = True)

    message = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return self.subject

class ProfessionList(models.Model):
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profession =  models.CharField(max_length = 200, null = True)
    birthday = models.DateField(null = True)
    gender =  models.CharField(max_length = 200, null = True)
    phone =  models.CharField(max_length = 200, null = True)
    city =  models.CharField(max_length = 200, null = True)
    pincode =  models.CharField(max_length = 200, null = True)

    class Meta:
        db_table: "professionlist"

    def __str__(self):
        return self.profession


class Rent(models.Model):
     
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 200, null = True)
    status = models.CharField(max_length = 200, null = True)
    rent_item = models.CharField(max_length = 200, null = True)
    its_name = models.CharField(max_length = 200, null = True)
    contact_no = models.CharField(max_length = 200, null = True)
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    address = models.CharField(max_length = 1000, null = True)


    def __str__(self):
        return self.its_name

class Hire(models.Model):
     

    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 200, null = True)
    service = models.CharField(max_length = 200, null = True)
    contact_no = models.CharField(max_length = 200, null = True)
    date_needed = models.DateField(null = True)
    address = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return self.service




        
    
    

