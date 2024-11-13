from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import *


def paginate(object_list, request, per_page):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(object_list, per_page)
    return paginator.page(page_num)


# Create your views here.
def questions_listing(request):
    questions = Question.objects.get_new_questions()
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()
    page = paginate(list(questions), request, per_page=20)

    return render(request, "index.html",
                  context={"questions": page.object_list, 'page_obj': page, "tags": tags, "best_members": best_members})


def hot_questions(request, is_hot):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()
    if is_hot == "hot":
        questions = Question.objects.get_hot_questions()
        return render(request, "index.html",
                      context={"hot": is_hot, "questions": questions, "tags": tags, "best_members": best_members})
    else:
        return render(request, "404.html", status=404, context={"tags": tags, "best_members": best_members})


def tag_questions(request, tag):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()
    questions_tag = Question.objects.get_questions_with_tag(tag)
    page = paginate(list(questions_tag), request, per_page=20)

    return render(request, "index.html",
                  context={"tag": tag, "questions": page.object_list, 'page_obj': page, "tags": tags,
                           "best_members": best_members})


def question(request, id):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()
    card_question = Question.objects.get(id=id)
    answers = Answer.objects.get_answers_by_question_id(id)
    page = paginate(list(answers), request, per_page=30)

    return render(request, "question.html",
                  context={"question": card_question, "answers": page.object_list, 'page_obj': page, "tags": tags,
                           "best_members": best_members})


def new_question(request):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()

    return render(request, "ask.html", context={"tags": tags, "best_members": best_members})


def login(request):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()

    return render(request, "login.html", context={"tags": tags, "best_members": best_members})


def signup(request):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()

    return render(request, "signup.html", context={"tags": tags, "best_members": best_members})


def settings(request):
    tags = Tag.objects.get_tags()
    best_members = Profile.objects.get_best_members()

    return render(request, "settings.html", context={"tags": tags, "best_members": best_members})
