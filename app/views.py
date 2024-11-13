from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import *

# questions = []
# for i in range(140):
#     questions.append({
#         'title': 'title ' + str(i),
#         'id': i,
#         'text': 'text ' + str(i),
#         'tags': ['tag ' + str(i)],
#         'answers': [{
#             'answer_text': 'answer ' + str(i),
#             'answer_rating': i
#         } for _ in range(150)]
#     })
#
# tags = []
# for i in range(1, 30):
#     tags.append({
#         'tag': ('tag ' + str(i))
#     })

# best_members = [
#     "Mr. Freeman",
#     "Dr. House",
#     "Bender",
#     "Queen Victoria",
#     "V. Pupkin"
# ]


def paginate(object_list, request, per_page):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(object_list, per_page)
    return paginator.page(page_num)


# Create your views here.
def questions_listing(request):
    questions = Question.objects.get_new_questions()
    tags = Tag.objects.get_tags()
    page = paginate(questions, request, per_page=20)
    best_members = Profile.objects.get_best_members()
    return render(request, "index.html",
                  context={"questions": page.object_list, 'page_obj': page, "tags": tags, "best_members": best_members})


def hot_questions(request, is_hot):
    if is_hot == "hot":
        return render(request, "index.html",
                  context={"hot": is_hot, "questions": questions, "tags": tags, "best_members": best_members})
    else:
        return render(request, "404.html", status=404, context={"tags": tags, "best_members": best_members})


def tag_questions(request, tag):
    questions_tag = []
    for question in questions:
        for question_tag in question['tags']:
            if question_tag == tag:
                questions_tag.append(question)
    page = paginate(questions_tag, request, per_page=20)
    return render(request, "index.html",
                  context={"tag": tag, "questions": page.object_list, 'page_obj': page, "tags": tags, "best_members": best_members})


def question(request, id):
    card_question = questions[id]
    page = paginate(card_question['answers'], request, per_page=30)
    return render(request, "question.html",
                  context={"question": card_question, "answers": page.object_list, 'page_obj': page, "tags": tags,
                           "best_members": best_members})


def new_question(request):
    return render(request, "ask.html", context={"tags": tags, "best_members": best_members})


def login(request):
    return render(request, "login.html", context={"tags": tags, "best_members": best_members})


def signup(request):
    return render(request, "signup.html", context={"tags": tags, "best_members": best_members})


def settings(request):
    return render(request, "settings.html")
