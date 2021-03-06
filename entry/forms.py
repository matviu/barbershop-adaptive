# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
from django.forms.utils import ErrorList
from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ['date_added']
        widgets = {
            'last_name': widgets.TextInput(attrs={
                'class': 'appointment__text-field text-field',
                'placeholder': u'Фамилия'
            }),
            'first_name': widgets.TextInput(attrs={
                'class': 'appointment__text-field text-field',
                'placeholder': u'Имя'
            }),
            'second_name': widgets.TextInput(attrs={
                'class': 'appointment__text-field text-field',
                'placeholder': u'Отчество'
            }),
            'tel_number': widgets.TextInput(attrs={
                'class': 'appointment__text-field text-field',
                'placeholder': u'Контактный телефон'
            }),
            'email': widgets.TextInput(attrs={
                'class': 'appointment__text-field text-field',
                'placeholder': u'Контактный email'
            }),
            'add_info': widgets.Textarea(attrs={
                'class': 'text-field appointment__add-info',
                'placeholder': u'Допю информация для мастера'
            }),
            'beard_model': widgets.RadioSelect(attrs={
                'class': 'invisible-radiobox'
            }),
            'is_beard_paint': widgets.CheckboxInput(attrs={
                'class': 'invisible-checkbox'
            }),
            'is_beard_brush': widgets.CheckboxInput(attrs={
                'class': 'invisible-checkbox'
            }),
            'is_remove_gray': widgets.CheckboxInput(attrs={
                'class': 'invisible-checkbox'
            }),
            'is_moustache_spin': widgets.CheckboxInput(attrs={
                'class': 'invisible-checkbox'
            }),
            'is_trim': widgets.CheckboxInput(attrs={
                'class': 'invisible-checkbox'
            }),
            'is_polish_head': widgets.CheckboxInput(attrs={
                'class': 'invisible-checkbox'
            }),
            'date_record': widgets.DateTimeInput(attrs={
                'class': 'appointment__text-field text-field',
                'placeholder': u'Дата и время записи в формате гггг-мм-дд чч:мм'
            }),
        }


