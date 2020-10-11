from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(TutoriaUser)
#admin.site.register(Department)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(SubjectTag)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Admin)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(Coupon)
admin.site.register(BlackOutTimeSlot)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Transaction)
admin.site.register(passwordToken)
admin.site.register(Conversation)