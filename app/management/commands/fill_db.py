from django.core.management.base import BaseCommand

from app.models import *


# QUESTION_RATIO = 10
# ANSWER_RATIO = 100
# RATING_RATIO = 200


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **kwargs):
        ratio = int(kwargs['ratio'])

        users = [User(username=f'login_{str(i)}', email=f'email{str(i)}@gmail.com', password=f'{str(i) * 6}') for i in
                 range(ratio)]
        User.objects.bulk_create(users)

        profiles = [Profile(user_id=user, nickname=f'user_nickname_{str(i)}') for i, user in enumerate(users)]
        Profile.objects.bulk_create(profiles)

        questions = [Question(profile_id=profile, title=f'title_{str(i)}', text=f'text_{str(i)}') for i, profile
                     in enumerate(profiles)]
        Question.objects.bulk_create(questions)

        tags = [Tag(question_id=question, name=f'tag_{str(i)}') for i, question in enumerate(questions)]
        Tag.objects.bulk_create(tags)

        answers = [Answer(question_id=question, profile_id=profile, text=f'text_{str(i)}') for i, (question, profile) in
                   enumerate(zip(questions, profiles))]
        Answer.objects.bulk_create(answers)

        answer_likes = [AnswerLike(profile_id=profile, answer_id=answer) for i, (profile, answer) in
                        enumerate(zip(profiles, answers))]
        AnswerLike.objects.bulk_create(answer_likes)

        question_likes = [QuestionLike(profile_id=profile, question_id=question) for i, (profile, question) in
                          enumerate(zip(profiles, questions))]
        QuestionLike.objects.bulk_create(question_likes)
