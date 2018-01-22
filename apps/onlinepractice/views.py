# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserErrorQuestion, UserPractice
from utils.mixin_utils import LoginRequiredMixin
# Create your views here.

class QuestionBankView(View):
    '''
    题库列表页
    '''
    def get(self, request):
        question_banks = QuestionBank.objects.all()

         #对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(question_banks, 6, request=request)

        question_banks = p.page(page)

        return render(request, 'practice-list.html', locals())

class PracticeBankDetailView(View):
    '''
    题库详情页
    TODO：页面右下角展示的相关题库
    '''

    def get(self, request, practice_bank_id):
        question_bank = QuestionBank.objects.get(id=practice_bank_id)
        return render(request, 'practice-bank-detail.html', locals())


class PracticeChoiceDetailView(View):
    '''
    选择题详情页
    '''
    def get(self, request, practice_bank_id, practice_num):
        is_last_question = False
        question_bank = QuestionBank.objects.get(id=practice_bank_id)
        question = ChoiceQuestion.objects.get(question_num=practice_num, questionBank=question_bank)
        next_practice_num = str(int(practice_num) + 1)
        if practice_num == '1':
            #分数清0
            request.session['user_score'] = 0
        try:
            next_question = ChoiceQuestion.objects.get(question_num=next_practice_num, questionBank=question_bank)
        except ChoiceQuestion.DoesNotExist as e:
            is_last_question = True
        return render(request, 'practice-choice-detail.html', locals())


class PracticeChoiceSubmit(View):
    def post(self, request):
        answer_list = ['A', 'B', 'C', 'D']
        user_answer = request.POST.get('user_answer')
        practice_num = request.POST.get('practice_num')
        practice_bank_id = request.POST.get('practice_bank_id')
        print user_answer, practice_num
        if user_answer != '-1':
            #查询正确答案
            questionBank = QuestionBank.objects.get(id=practice_bank_id)
            question = ChoiceQuestion.objects.get(question_num=practice_num, questionBank=questionBank)
            correct_answer = question.answer
            #判断用户是否答对
            if answer_list[int(user_answer)]==correct_answer:
                #答对则更新分数session
                request.session['user_score'] = request.session.get('user_score',default=0) + 1
            else:
                #答错则存储到用户错题集
                user = request.user
                try:
                    UserErrorQuestion.objects.get(user=user, question=question)
                except UserErrorQuestion.DoesNotExist:
                    user_error_question = UserErrorQuestion()
                    user_error_question.user = user
                    user_error_question.question = question
                    user_error_question.save()
            return HttpResponse('{"status":"success", "msg":"提交成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"没有进行选择"}', content_type='application/json')


class PracticeChoiceResult(LoginRequiredMixin, View):
    def get(self, request, practice_bank_id, practice_complete_num):
        question_bank = QuestionBank.objects.get(id=practice_bank_id)
        score =  request.session.get('user_score',default=0)
        if score:
            correct_percent = score*100/question_bank.choicequestion_set.all().count()
        else:
            correct_percent = 0
        #保存用户作业完成情况
        #首先查询该用户是否有该题库记录
        try:
            user_practice = UserPractice.objects.get(user=request.user, practice_bank_id=practice_bank_id)
        except UserPractice.DoesNotExist:
            #没有该信息则存储题库数据
            user_practice = UserPractice()
            user_practice.user = request.user
            user_practice.practice_bank_id = practice_bank_id
            user_practice.practice_num = practice_complete_num
            user_practice.practice_bank_correct_percent = correct_percent
            user_practice.save()

        else:
            #有该信息则更新题库数据
            user_practice.practice_num = practice_complete_num
            user_practice.practice_bank_correct_percent = correct_percent
            user_practice.save()

        return render(request, 'practice-choice-result.html', locals())


class ProgramDetailView(LoginRequiredMixin, View):
    '''
    编程题详情页
    '''
    def get(self, request, practice_bank_id, practice_num):

        is_last_question = False
        question_bank = QuestionBank.objects.get(id=practice_bank_id)
        question = ProgramQuestion.objects.get(question_num=practice_num, questionBank=question_bank)
        next_practice_num = str(int(practice_num) + 1)
        try:
            next_question = ProgramQuestion.objects.get(question_num=next_practice_num, questionBank=question_bank)
        except ProgramQuestion.DoesNotExist as e:
            is_last_question = True

        return render(request, 'program-detail.html', locals())


class ProgramResult(LoginRequiredMixin, View):
    def get(self, request, practice_bank_id, practice_complete_num):
        question_bank = QuestionBank.objects.get(id=practice_bank_id)
        #保存用户作业完成情况
        #首先查询该用户是否有该题库记录
        try:
            user_practice = UserPractice.objects.get(user=request.user, practice_bank_id=practice_bank_id)
        except UserPractice.DoesNotExist:
            #没有该信息则存储题库数据
            user_practice = UserPractice()
            user_practice.user = request.user
            user_practice.practice_bank_id = practice_bank_id
            user_practice.practice_num = practice_complete_num
            user_practice.save()

        else:
            #有该信息则更新题库数据
            user_practice.practice_num = practice_complete_num
            user_practice.save()


        return render(request, 'program-result.html', locals())