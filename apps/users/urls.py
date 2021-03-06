# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.conf.urls import url, include

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView, \
    MyPracticeCount, MyPracticeComment, MyPracticeErrors, UserQuestionAnswer, UserQuestionAnswered, \
    UserQuestionWillAnswer, UserQuestionDetail

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    # 我收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),
    # 我的作业统计
    url(r'^mypractice/count/$', MyPracticeCount.as_view(), name="my_practice_count"),
    # 我的提交点评
    url(r'^mypractice/commnet/$', MyPracticeComment.as_view(), name="my_practice_comment"),
    # 我的错题集
    url(r'^mypractice/error/$', MyPracticeErrors.as_view(), name="my_practice_error"),
    #老师已回答问题
    url(r'^my_question_answered/$', UserQuestionAnswered.as_view(), name='my_question_answered'),
    #老师未回答问题
    url(r'^my_question_will_answer/$', UserQuestionWillAnswer.as_view(), name='my_question_will_answer'),
    # 我的提问详情页
    url(r'^my_question_detail/(?P<user_question_id>\d+)/$', UserQuestionDetail.as_view(), name='my_question_detail'),

]
