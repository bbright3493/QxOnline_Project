# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2016/10/25 23:59'
import xadmin

from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite, UserTeacher, UserQuestionTeacher

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    model_icon = 'fa fa-question-circle'


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    model_icon = 'fa fa-address-book'

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-envelope-o'


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']
    model_icon = 'fa fa-comment'


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    model_icon = 'fa fa-heart'


class UserTeacherAdmin(object):
    list_display = ['user', 'teacher']
    search_fields = ['user', 'teacher']
    list_filter = ['user', 'teacher']
    model_icon = 'fa fa-heart'


class UserQuestionTeacherAdmin(object):
    list_display = ['user', 'question_content', 'teacher', 'answer', 'question_status']
    search_fields = ['user', 'question_content', 'teacher', 'answer', 'question_status']
    list_filter = ['user', 'question_content', 'teacher', 'answer', 'question_status']
    model_icon = 'fa fa-heart'
    style_fields = {"answer": "ueditor"}

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserTeacher, UserTeacherAdmin)
xadmin.site.register(UserQuestionTeacher, UserQuestionTeacherAdmin)

