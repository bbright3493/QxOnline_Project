# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from datetime import datetime
from courses.models import Lesson


class ChoiceQuestion(models.Model):
    question_num = models.IntegerField(verbose_name=u'题目编号')
    question_content = models.CharField(max_length=500, verbose_name=u'题目内容')
    choiceA = models.CharField(max_length=200, verbose_name=u'选项A')
    choiceB = models.CharField(max_length=200, verbose_name=u'选项B')
    choiceC = models.CharField(max_length=200, verbose_name=u'选项C')
    choiceD = models.CharField(max_length=200, verbose_name=u'选项D')
    answer = models.CharField(max_length=2, verbose_name=u'答案')
    explain = models.CharField(max_length=800, verbose_name=u'答案解释')
    questionBank = models.ForeignKey("QuestionBank", verbose_name=u'所属题库')

    class Meta:
        verbose_name = u'选择题'
        verbose_name_plural = verbose_name


class QuestionBank(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'题库名称')
    desc = models.CharField(max_length=200, verbose_name=u'题库描述', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    lesson = models.ForeignKey(Lesson, verbose_name=u"课程章节")
    degree = models.CharField(verbose_name=u"难度", choices=(("cj","初级"), ("zj","中级"), ("gj","高级")), max_length=2, null=True, blank=True)
    complete_times = models.IntegerField(default=0, verbose_name=u"建议完成时长(分钟数)")
    image = models.ImageField(upload_to="onlinepractice/%Y/%m", verbose_name=u"封面图", max_length=100, null=True, blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    type = models.CharField(verbose_name=u"题库类别", choices=(("xzt","选择题"), ("bct","编程题")), max_length=5, null=True, blank=True)
    detail = models.CharField(max_length=300, verbose_name=u'题库详情', null=True, blank=True)

    class Meta:
        verbose_name = u'题库'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class ProgramQuestion(models.Model):
    question_num = models.IntegerField(verbose_name=u'题目编号')
    question_content = models.CharField(max_length=500, verbose_name=u'题目内容')
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"源码文件", max_length=100)
    url = models.CharField(max_length=200, default="", verbose_name=u"题目讲解视频地址")
    essentials = models.CharField(max_length=500, verbose_name=u'题目要点')
    questionBank = models.ForeignKey("QuestionBank", verbose_name=u'所属题库', blank=True, null=True)

    class Meta:
        verbose_name = u'编程题'
        verbose_name_plural = verbose_name

