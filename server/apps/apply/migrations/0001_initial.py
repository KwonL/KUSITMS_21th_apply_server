# Generated by Django 3.0.7 on 2021-02-03 05:41

import apps.apply.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='학회원', max_length=255, verbose_name='지원서 타입(학회원, 경총, 대홍..)')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('notice', models.TextField(blank=True, default='', verbose_name='유의사항')),
                ('question_1', models.TextField(default='', verbose_name='질문 1')),
                ('question_2', models.TextField(default='', verbose_name='질문 2')),
                ('question_3', models.TextField(default='', verbose_name='질문 3')),
                ('question_4', models.TextField(default='', verbose_name='질문 4')),
                ('question_5', models.TextField(default='', verbose_name='질문 5(활동 내역)')),
                ('question_6', models.TextField(default='', verbose_name='질문 6(자유롭게 하고싶은 말)')),
                ('interview_start', models.DateTimeField(verbose_name='면접 시작일과 시간(한시간 단위로 설정됨)')),
                ('interview_end', models.DateTimeField(verbose_name='면접 종료일과 시간(한시간 단위로 설정됨)')),
            ],
            options={
                'db_table': 'apply_config',
            },
        ),
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.apply.models.get_image_name)),
                ('email', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('birth', models.DateField()),
                ('phone', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=2)),
                ('insta', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('answer_1', models.TextField(default='')),
                ('answer_2', models.TextField(default='')),
                ('answer_3', models.TextField(default='')),
                ('answer_4', models.TextField(default='')),
                ('answer_5', models.TextField(default='')),
                ('answer_6', models.TextField(default='')),
                ('activity_1', models.CharField(blank=True, max_length=255)),
                ('activity_2', models.CharField(blank=True, max_length=255)),
                ('activity_3', models.CharField(blank=True, max_length=255)),
                ('activity_4', models.CharField(blank=True, max_length=255)),
                ('activity_5', models.CharField(blank=True, max_length=255)),
                ('interview_date', models.TextField(blank=True, default='')),
                ('apply_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='apply.ApplyConfig')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.IntegerField(default=0, verbose_name='기수')),
                ('main_image', models.ImageField(default='', upload_to=apps.apply.models.get_main_image_name)),
                ('president', models.CharField(default='', max_length=100, verbose_name='학회장 이름 (전화번호)')),
                ('vice_president', models.CharField(default='', max_length=100, verbose_name='부학회장 이름 (전화번호)')),
                ('start', models.DateTimeField(verbose_name='지원 시작일')),
                ('end', models.DateTimeField(verbose_name='지원 종료일')),
                ('ot_date', models.DateField(verbose_name='OT 날짜')),
                ('mt_date', models.DateField(verbose_name='MT 날짜')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('recruitment_summary', models.URLField(blank=True, default='', verbose_name='모집 요강 URL')),
            ],
            options={
                'db_table': 'site_config',
            },
        ),
        migrations.CreateModel(
            name='SNSImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to=apps.apply.models.get_sns_image_name)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sns_images', to='apply.ApplyForm')),
            ],
        ),
        migrations.CreateModel(
            name='MainSlideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to=apps.apply.models.get_main_slide_name)),
                ('site_config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_slides', to='apply.SiteConfig')),
            ],
        ),
    ]
