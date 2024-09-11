from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView, UpdateView, DeleteView


def index_view(request):
    model_info = Cards_model.objects.all()
    context = {
        'model_info': model_info,
    }
    return render(request, 'main/Main.html', context)

def photoGalery_view(request):
    model_info = PhotoGalery_model.objects.all()
    context = {
        'model_info': model_info,
    }
    return render(request, 'main/PhotoGalery.html', context)

def videoGalery_view(request):
    model_info = VieoGalery_model.objects.all()
    context = {
        'model_info': model_info,
    }
    return render(request, 'main/VideoGalery.html', context)

def educationKPK_view(request):
    model_info = Diploms_model.objects.all()
    context = {
        'model_info': model_info,
    }
    return render(request, 'main/EducationKPK.html', context)


def achievements_view(request):
    # Создали словарик achievements_by_year, в котором года будут
    achievements_by_year = {}
    achievements = Dostijenia_model.objects.all()

    for achievement in achievements:
        year = achievement.Year
        # Создаём список годов, к которым добавляем содержимое
        if year not in achievements_by_year:
            achievements_by_year[year] = []
        achievements_by_year[year].append(achievement)

    # Сортируем словарь по убыванию года
    achievements_by_year = dict(sorted(achievements_by_year.items(), reverse=True))

    context = {
        'achievements_by_year': achievements_by_year,
    }
    return render(request, 'main/Achievement.html', context)


def StudentAchievements_view(request):
    # Создали словарик achievements_by_year, в котором года будут
    achievements_by_year = {}
    achievements = DostijeniaSchoolboy_model.objects.all()

    for achievement in achievements:
        year = achievement.Year
        # Создаём список годов, к которым добавляем содержимое
        if year not in achievements_by_year:
            achievements_by_year[year] = []
        achievements_by_year[year].append(achievement)

    # Сортируем словарь по убыванию года
    achievements_by_year = dict(sorted(achievements_by_year.items(), reverse=True))

    context = {
        'achievements_by_year': achievements_by_year,
    }
    return render(request, 'main/StudentAchievement.html', context)

