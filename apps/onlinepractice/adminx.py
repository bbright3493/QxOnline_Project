#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author:
import xadmin
from .models import *


class ChoiceQusetionAdmin(object):
    list_display = ['question_num', 'question_content', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'answer', 'explain', 'questionBank']
    search_fields = ['question_num', 'question_content', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'answer', 'explain', 'questionBank']
    list_filter = ['question_num', 'question_content', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'answer', 'explain', 'questionBank']

xadmin.site.register(ChoiceQuestion, ChoiceQusetionAdmin)


class ProgramQuestionAdmin(object):
    list_display = ['question_num', 'question_content', 'download', 'url', 'essentials', 'questionBank']
    search_fields = ['question_num', 'question_content', 'download', 'url', 'essentials', 'questionBank']
    list_filter = ['question_num', 'question_content', 'download', 'url', 'essentials', 'questionBank']

xadmin.site.register(ProgramQuestion, ProgramQuestionAdmin)


class QuestionBankAdmin(object):
    list_display = ['name', 'add_time', 'click_nums', 'lesson']
    search_fields = ['name', 'click_nums', 'lesson']
    list_filter = ['name', 'click_nums', 'lesson']

xadmin.site.register(QuestionBank, QuestionBankAdmin)




