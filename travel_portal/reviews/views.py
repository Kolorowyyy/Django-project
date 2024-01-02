from django.shortcuts import render
from .models import Review, Rating


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def rating_list(request):
    ratings = Rating.objects.all()
    return render(request, 'reviews/rating_list.html', {'ratings': ratings})
