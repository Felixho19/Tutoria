from __future__ import unicode_literals
from datetime import date,datetime
from django.db import models
from django import forms
# Create your models here.

class UserTutoria(models.Model):
    GENDER_LIST = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    username = models.CharField(max_length=255)
    def __str__(self):
        return self.username
    def is_login(self):
        return True
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_LIST)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=255)
    isActive = models.IntegerField()
    #coins = models.DecimalField(max_digits=255, decimal_places=1)
    is_student = models.IntegerField()
    is_tutor = models.IntegerField()
    def getFullName(self):
        return str(self.firstName) + ' ' + str(self.lastName)
    '''
    def make_transaction(self, amount, type):
        #userObj = UserTutoria.objects.get(id=userID)
        #make transaction
        t = Transaction.objects.create(userID=self, totalPayment=amount, description=str(type))
        t.save()
        #make notification
        if amount >=0:
            message = "$"+str(amount) + " has been added to your wallet"
        else:
            message = "$"+str(-amount) + " has been removed from your wallet" 
        n= Notification.objects.create(userID=self, notificationDetails=message)
        #pusher_client.trigger('my-channel-'+str(userID), 'notification', {'message': 'added new notification'})
        n.save()
    '''

class Student(models.Model):
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.userID.id)

class University(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
def get_image_file_name(instance, filename):
    return "media/%s" %(instance.userID.id)
    
class Tutor(models.Model):
    '''TUTOR_TYPE = (
        ('contracted', 'contracted'),
        ('regular', 'in regular'),
    )'''
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.userID.id)
    universityID = models.ForeignKey(University, on_delete=models.CASCADE)
    hourlyRate = models.IntegerField()
    #tutorAvatar = models.CharField(max_length=255)
    #tutorAvatar = models.ImageField(upload_to='media/',null=True, blank=True)
    tutorAvatar = models.ImageField(upload_to=get_image_file_name,null=True, blank=True)
    tutorType = models.IntegerField() # 0: regular tutor 1: contracted tutor
    biography = models.CharField(max_length=255)

class Department(models.Model):
    universityID = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
     
class CourseCode(models.Model):
    courseCode = models.CharField(max_length=255)
    departmentID = models.ForeignKey(Department, on_delete=models.CASCADE)
    universityID = models.ForeignKey(University, on_delete=models.CASCADE)
    def __str__(self):
        return self.courseCode

class Session(models.Model):
    STATUS_LIST = (
        #('available', 'available'),
        ('booked', 'booked'),
        ('locked', 'locked'),
        ('completed', 'completed'),
        ('incomplete', 'incomplete'),
        ('reviewed', 'reviewed')
        #('start', 'begin'),
        #('now', 'in progress'),
        #('end', 'end'),
    )
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    status = models.CharField(max_length=255, choices=STATUS_LIST,null=True, blank=True) # 0: begin, 2: in progress, 3: ended (booked and ended)
    universityID = models.ForeignKey(University, on_delete=models.CASCADE)
    tutorID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return str(self.id)
    
class Transaction(models.Model):
    DESCRIPTION_LIST=(
        ('0', 'addCoins'),
        ('1', 'removeCoins'),
        ('2', 'sessionPayment'),
        ('3', 'sessionSalary'),
        ('4', 'sessionRefund'),
    )
    description = models.CharField(max_length=2, choices=DESCRIPTION_LIST,null=True, blank=True)
    totalPayment = models.IntegerField()
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True, blank=True)
    sessionID = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    '''
    is_debit = models.IntegerField()
    is_credit = models.IntegerField()
    '''
    couponCode = models.CharField(max_length=255, null=True, blank=True)
    ordering = ['date', 'time']

class CourseTaughtByTutor(models.Model):
    tutorID = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    courseID = models.ForeignKey(CourseCode, on_delete=models.CASCADE)
    
class Notification(models.Model):
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    notificationDetails = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True, blank=True)
    
class Message(models.Model):
    receiverID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE, related_name='message_receiver')
    senderID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE, related_name='message_sender')
    content = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    
class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    isActive = models.IntegerField()
    coins = models.DecimalField(max_digits=255, decimal_places=1)

class Coupon(models.Model):
    couponCode = models.CharField(max_length=255)
    startTime = models.TimeField()
    endTime = models.TimeField()
    def __str__(self):
        return self.couponCode

# Tutor is using this part as making his.her timeslot unavailable to the student
# Student cannot select the time slot that tutor blocked (filter all bdate,time by userID)
class BlackOutTimeSlot(models.Model):
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    bdate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    
class Review(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=255, null=True, blank=True)
    
class SubjectTag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Tagging(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    tag = models.ForeignKey(SubjectTag, on_delete=models.CASCADE)
    
class passwordToken(models.Model):
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    createDate = models.DateField(default=date.today)
    
"""class ActivationToken(models.Model):
    userID = models.ForeignKey(UserTutoria, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    createDate = models.DateField(default=date.today)"""