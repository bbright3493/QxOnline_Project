#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: Artorias
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^list', QuestionBankView.as_view(), name='practice_list'),
    url(r'^detail/(?P<practice_bank_id>\d+)/$', PracticeBankDetailView.as_view(), name='practice_bank_detail'),
    url(r'^choice_detail/(?P<practice_bank_id>\d+)/(?P<practice_num>\d+)/$', PracticeChoiceDetailView.as_view(), name='practice_choice_detail'),
    url(r'^choice_detail_explain/(?P<practice_bank_id>\d+)/(?P<practice_num>\d+)/$', PracticeChoiceDetailExplainView.as_view(), name='practice_choice_detail_explain'),
    url(r'^program_detail/(?P<practice_bank_id>\d+)/(?P<practice_num>\d+)/$', ProgramDetailView.as_view(), name='program_detail'),
    url(r'^choice_detail_submit/$', PracticeChoiceSubmit.as_view(), name='choice_detail_submit'),
    url(r'^choice_result/(?P<practice_bank_id>\d+)/(?P<practice_complete_num>\d+)/$', PracticeChoiceResult.as_view(), name='practice_choice_result'),
    url(r'^program_result/(?P<practice_bank_id>\d+)/(?P<practice_complete_num>\d+)/$', ProgramResult.as_view(), name='program_result'),
    url(r'^program_comment/(?P<practice_id>\d+)/$', ProgramComment.as_view(), name='program_comment'),
    url(r'^program_submit/(?P<practice_id>\d+)/$', ProgramSubmit.as_view(), name='program_submit'),

]
