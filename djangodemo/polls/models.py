import datetime

from django.db import models

from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    des = models.CharField(max_length=200)
    salary = models.IntegerField()
    joining_date = models.DateTimeField('joining_date')

    def __str__(self):
        return self.emp_name

    def date_join(self):
        return self.joining_date >= timezone.now() - datetime.timedelta(days=1)


class Project(models.Model):
    pr_name = models.CharField(max_length=200)
    pr_no = models.IntegerField(default=1)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.pr_name
