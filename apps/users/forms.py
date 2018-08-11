#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-24 下午2:42
# @Author  : Shark
# @File    : forms.py
# @Software: PyCharm
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    user_name = forms.CharField(required=True)
    # captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
