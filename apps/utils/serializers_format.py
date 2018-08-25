#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-25 下午9:35
# @Author  : Shark
# @File    : serializers_format.py
# @Software: PyCharm


def value_format(queryset):
    from apps.major.models import Image
    img = Image.objects.filter(ChapterTask_name=queryset.chapter_name.id).all()
    image = []
    for i in img:
        image.append(i.image.url if i.image else None)

    return {
                'id': queryset.id,
                'chapter_name': queryset.chapter_name,
                'name': queryset.name,
                'info': queryset.info,
                'image': image,
                'add_time': queryset.add_time
            }

