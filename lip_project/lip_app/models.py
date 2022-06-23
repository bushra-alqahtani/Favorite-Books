from django.db import models
import re
import bcrypt



# Create your models here.
class UserManager(models.Manager):
    def validatorRe(self,postData):
        
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            errors={}
        
            #checking first name & last name:
            if len(postData['First_Name'])<2:
                errors['First_Name']=" first name should be more than 2 chars"
            if len(postData['Last_Name'])<2:
                errors['Last_Name']="last name must be more than 2 chars"

            #checking password:
            if len(postData['Password']) < 8:
                errors['Password'] = "Password should be at least 8 characters"
            if postData['Password'] != postData['Password2']:
                errors['pw_match'] = "Passwords don't match "

            
            #checking email: 
            if not EMAIL_REGEX.match(postData['Email']):    # test whether a field matches the pattern            
                errors['Email'] = "Invalid email address!"
            return errors

                
    def validatorLo(self,postData):
            errors = {}
            #fetching for the email in db.
            user = Users.objects.filter(Email=postData['Email'])

            #checking email (if user=none -> error , if user exist -> else)
            if not(user):
                errors ['Email'] = 'Email is not correct'
            elif not(bcrypt.checkpw(postData['Password'].encode(), user[0].Password.encode())):
                errors ['Password'] = 'Not correct password'
            
            return errors
            
class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['desc'])<5:
                errors['desc']="descripthion must be at least 5 cars "
        if len(postData['title'])==0:
                errors['title']=" title is required"
        return errors






class Users(models.Model):
    First_Name=models.CharField(max_length=255)
    Last_Name=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    user = models.ForeignKey(Users, related_name='books', on_delete=models.CASCADE)
    users_like =models.ManyToManyField(Users, related_name="books_like")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects=BookManager()




