# coding:utf-8
from __future__ import unicode_literals

from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    # name = forms.CharField(max_length=128, label='姓名')
    # sex = forms.IntegerField(choices=Student.STATUS_ITEMS, label='性别')
    # profession = forms.CharField(max_length=128, label='职业')
    # email = forms.EmailField(label="邮件", max_length=128)
    # qq = forms.CharField(max_length=128, label='QQ')
    # phone = forms.CharField(max_length=128, label='手机')
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )
