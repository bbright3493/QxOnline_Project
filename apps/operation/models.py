# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course
from onlinepractice.models import ChoiceQuestion, ProgramQuestion, QuestionBank
from DjangoUeditor.models import UEditorField
from organization.models import Teacher

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


class UserPracticeComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    program = models.ForeignKey(ProgramQuestion, verbose_name=u'点评的编程题')
    upload = models.FileField(upload_to="onlinepractice/upload/%Y/%m", verbose_name=u"用户源码", max_length=100, default='')
    comment = UEditorField(verbose_name=u"老师点评",width=600, height=300, imagePath="operation/ueditor/",
                                         filePath="operation/ueditor/", default='')
    level = models.CharField(verbose_name=u"评分等级", choices=(("wm","完美"), ("yx","优秀"), ("lh","良好"), ("hg","合格"),("bhg","不合格")), max_length=8)
    teacher = models.ForeignKey(Teacher, verbose_name=u"点评讲师")
    comment_status = models.IntegerField(choices=((1,"已点评"), (0,"未点评")), default=0, verbose_name=u'是否已经点评')
    user_submit_time = models.DateTimeField(default=datetime.now, verbose_name=u"作业提交时间")
    teacher_comment_time = models.DateTimeField(default=datetime.now, verbose_name=u"老师点评时间")
    class Meta:
        verbose_name = u'用户的作业点评'
        verbose_name_plural = verbose_name


class UserQuestionTeacher(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"提问用户")
    question_content = models.CharField(max_length=1000, default=u'', verbose_name=u'提问内容')
    teacher = models.ForeignKey(Teacher, verbose_name=u"回答讲师")
    answer = UEditorField(verbose_name=u"老师回答",width=600, height=300, imagePath="operation/ueditor/",
                                         filePath="operation/ueditor/")
    question_status = models.IntegerField(choices=((1,"已回答"), (0,"未回答")), default=0, verbose_name=u'是否已经回答')
    user_question_time = models.DateTimeField(default=datetime.now, verbose_name=u"提问时间")
    teacher_answer_time = models.DateTimeField(default=datetime.now, verbose_name=u"回答时间")
    class Meta:
        verbose_name = u'用户问题回答'
        verbose_name_plural = verbose_name


class UserTeacher(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师")

    class Meta:
        verbose_name = u'讲师用户表'
        verbose_name_plural = verbose_name

