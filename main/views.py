from django.shortcuts import render


def show_main(request):
    context = {"npm": "2306275185", "name": "Fadiansah Feryan Fatha", "class": "PBP A"}
    return render(request, "main.html", context)
