from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileManager(models.Manager):
    def get_best_members(self):
        return self.all()[:6]

class Profile(models.Model):
    user_id = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    avatar = models.ImageField(null=True, blank=True)

    objects = ProfileManager()


class QuestionManager(models.Manager):
    def get_hot_questions(self):
        pass

    def get_new_questions(self):
        return self.filter(created_at__lte=datetime.now())


class Question(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(unique=True, max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()


class Answer(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class TagManager(models.Manager):
    def get_tags(self):
        return self.all()[:50]

class Tag(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=10)

    objects = TagManager()


class QuestionLike(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['profile_id', 'question_id'], name='unique_profile_question'),
        ]


class AnswerLike(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['profile_id', 'answer_id'], name='unique_profile_answer'),
        ]
