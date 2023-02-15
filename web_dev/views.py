from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def genre_list(request):
    with open('genres.txt') as f:
        genres = [line.strip() for line in f]

    context = {'genres': genres}
    return render(request, 'genres/genre_list.html', context)