# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course
from onlinepractice.models import ChoiceQuestion, ProgramQuestion, QuestionBank

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    "课程评论"
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")), default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name


class UserErrorQuestion(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    question = models.ForeignKey(ChoiceQuestion, verbose_name=u'错题')

    class Meta:
        verbose_name = u'用户错题'
        verbose_name_plural = verbose_name


class UserUploadProgram(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    program = models.ForeignKey(ProgramQuestion, verbose_name=u'编程题')
    upload = models.FileField(upload_to="onlinepractice/upload/%Y/%m", verbose_name=u"用户源码", max_length=100, default='')


class UserPractice(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    practice_bank_id = models.IntegerField(default=0, verbose_name=u'题库id')
    practice_num = models.IntegerField(default=0, verbose_name=u'已完成最后题目题号')
    practice_bank_correct_percent = models.IntegerField(default=0, verbose_name=u'题库正确率')

    class Meta:
        verbose_name = u'用户作业情况'
        verbose_name_plural = verbose_name

    def get_practice_bank(self):
        practice_bank = QuestionBank.objects.get(id=self.practice_bank_id)
        return practice_bank

    def get_complete_persent(self):
        #通过题目获取题库的完成度
        practice_bank = QuestionBank.objects.get(id=self.practice_bank_id)
        if practice_bank.type == 'bct':
            question_count = practice_bank.programquestion_set.count()
        else:
            question_count = practice_bank.choicequestion_set.count()

        complete_percent = self.practice_num*100/question_count
        return complete_percent



