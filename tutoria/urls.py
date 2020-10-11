from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    
    #before login
    url(r'^index', views.indexPage, name='index'),
    url(r'^login', views.loginPage, name='login'),
    url(r'^validate_user', views.validate_user, name='validate_user'),
    url(r'^forget_password/validate_email', views.validate_email, name='validate_email'),
    url(r'^forget_password/$', views.forgetPassword, name='forgetPassword'),
    url(r'^forget_password/(?P<token>\w+)/$', views.isValidToken, name='isValidToken'),    
    url(r'^forget_password/(?P<token>\w+)/resetPassword$', views.resetPassword, name='resetPassword'),  
    
    #login session
    url(r'^logout_session/', views.logout_session, name='logout_session'),
    
    #after login
    url(r'^(?P<userID>\d+)/student_home/$', views.student_home, name='student_home'),
    url(r'^(?P<userID>\d+)/tutor_home/$', views.tutor_home, name='tutor_home'),
    #url(r'^checking', views.loginCheck, name='loginCheck'),
    url(r'(?P<userID>\d+)/student_tutor_profile/(?P<tutorUserID>\d+)/$', views.student_tutor_profile, name='student_tutor_profile'),
    url(r'(?P<userID>\d+)/my_profile/$', views.my_profile, name='my_profile'),
    url(r'(?P<userID>\d+)/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'update_info/$', views.update_info, name='update_info'),
    url(r'update_tutor_info/$', views.update_tutor_info, name='update_tutor_info'),
    url(r'change_password/$', views.change_password, name='change_password'),
    
    #function:
    #notification
    url(r'^(?P<userID>\d+)/notification_center/$', views.notificationCenter, name='notificationCenter'),
    url(r'^(?P<userID>\d+)/notification_center/getNotification$', views.getNotification, name='getNotification'),
    
    #booking
    url(r'(?P<userID>\d+)/student_booking/(?P<tutorUserID>\d+)$', views.student_booking, name='student_booking'),
    url(r'^(?P<userID>\d+)/student_home/getTutorsList', views.getTutorsList, name='getTutorsList'),
    #url(r'^tutor_home/getBlockedTime', views.getBlockedTime, name='getBlockedTime'),
    url(r'getBlockedTime', views.getBlockedTime, name='getBlockedTime'),
    url(r'cancelBlock', views.cancelBlock, name='cancelBlock'),
    url(r'^(?P<userID>\d+)/cancel_booking/$', views.student_cancel_booking, name='cancelBooking'),
    url(r'^(?P<userID>\d+)/cancel_booking/getBookedSession$', views.getBookedSession, name='getBookedSession'),
    
    #session management
    url(r'cancelSession$', views.cancelSession, name='cancelSession'),
    url(r'getFullSession', views.getFullSession, name='getFullSession'),
    url(r'tutor_home/blackTimeSlot', views.blackTimeSlot, name='blackTimeSlot'),
    #url(r'^student_booking/(?P<userID>\d+)/getSessions', views.getSessions, name='getSessions'),
    url(r'(?P<userID>\d+)/student_booking/getSessions', views.getSessions, name='getSessions'),
    url(r'(?P<userID>\d+)/student_booking/bookSession', views.bookSession, name='bookSession'),
    url(r'(?P<userID>\d+)/student_booking/checkCoupon', views.checkCoupon, name='checkCoupon'),
        
    #coins
    url(r'^(?P<userID>\d+)/wallet/$', views.wallet, name='wallet'),
    url(r'^(?P<userID>\d+)/wallet/getWalletTransactionHistory$', views.getWalletTransactionHistory, name='getWalletTransactionHistory'),
    url(r'^removecoin/(?P<userID>\d+)$', views.removeCoin, name='removeCoin'),
    url(r'^(?P<userID>\d+)/coins$', views.coins, name='coins'),
    url(r'^(?P<userID>\d+)/addCoin', views.addCoin, name='addCoin'),
    url(r'^(?P<userID>\d+)/withdraw', views.withdraw, name='withdraw'),

    #review/course history
    url(r'(?P<userID>\d+)/submit_review/(?P<tutorUserID>\d+)/(?P<bookingID>\d+)/$', views.student_submit_review, name='submit_review'),    
    url(r'(?P<userID>\d+)/submit_review/(?P<tutorUserID>\d+)/(?P<bookingID>\d+)/handle_review_submission/$', views.handle_review_submission, name='handle_review_submission$'),
    url(r'^(?P<userID>\d+)/course_history/$', views.course_history, name='course_history'),
    url(r'^(?P<userID>\d+)/course_history/getCourseHistory$', views.getCourseHistory, name='getCourseHistory'),
    
    #View or cancel booked session
    url(r'^(?P<userID>\d+)/session_detail/(?P<bookingID>\d+)/$', views.session_detail, name='session_detail'), 

    #registration
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration_student/$', views.registration_student, name='registration_student'),
    url(r'^registration_tutor/$', views.registration_tutor, name='registration_tutor'),
    url(r'^registration_student_tutor/$', views.registration_student_tutor, name='registration_student_tutor'),
    #registration function
    url(r'^registerNewStudent/$', views.registerNewStudent, name='registerNewStudent'),
    url(r'^registerNewTutor/$', views.registerNewTutor, name='registerNewTutor'),
    url(r'^registerNewStudentTutor/$', views.registerNewStudentTutor, name='registerNewStudentTutor'),
    #validation
    url(r'^usernameExist/$', views.usernameExist, name='usernameExist'),
    url(r'^emailExist/$', views.emailExist, name='emailExist'),
    
    #admin
    url(r'^tutoria_admin/login', views.admin_login, name='admin_login'),
    url(r'^tutoria_admin/logout_admin', views.logout_admin, name='logout_admin'),
    url(r'^tutoria_admin/admin_validate/', views.admin_validate, name='admin_validate'),
    url(r'^tutoria_admin/index$', views.adminIndex, name='adminIndex'),
    url(r'^tutoria_admin/getUserList', views.getUserList, name='getUserList'),
    url(r'^tutoria_admin/reset_password$', views.adminResetPasswordPage, name='adminResetPasswordPage'),
    url(r'^tutoria_admin/control_user_right$', views.controlUserRightPage, name='controlUserRightPage'),
    url(r'^tutoria_admin/changeUserActiveStatus', views.changeUserActiveStatus, name='changeUserActiveStatus'),
    #coupon
    url(r'^tutoria_admin/coupon/$', views.adminCoupon, name='adminCoupon'),
    url(r'^tutoria_admin/coupon/add_coupon/$', views.addCouponPage, name='addCouponPage'),
    url(r'^tutoria_admin/gen_coupon/$', views.gen_coupon, name='gen_coupon'),
    url(r'^tutoria_admin/manage_course/$', views.manage_course, name='manage_course'),
    url(r'^tutoria_admin/add_course/$', views.add_course, name='add_course'),
    url(r'^tutoria_admin/manage_course/getCourseCode$', views.getCourseCode, name='getCourseCode'),
    url(r'^tutoria_admin/manage_course/deleteCourseCode$', views.deleteCourseCode, name='deleteCourseCode'),
    url(r'^tutoria_admin/manage_course/add_new_course/$', views.add_new_course, name='add_new_course'),
    url(r'^tutoria_admin/coupon/getCouponCode$', views.getCouponCode, name='getCouponCode'),
    #url(r'test', views.test, name='test'),#for testing bootstrap
    
    
    #testing websocket
    url(r'websocket_test/(?P<userID>\d+)$', views.websocket_test, name='websocket_test'),
    
    #message
    url(r'message/(?P<userID>\d+)$', views.messagePage, name='messagePage'),
    url(r'message/getMessageHistory$', views.getMessageHistory, name='getMessageHistory'),
    url(r'message/sendMessage', views.sendMessage, name='sendMessage'),
    url(r'message/getLastMessageAndFriendList', views.getLastMessageAndFriendList, name='getLastMessageAndFriendList'),
    
]
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)from django.conf.urls import url
'''