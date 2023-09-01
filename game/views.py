from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.method == "POST":
        room_code = request.POST.get("room_code")
        char_choice = request.POST.get("char_choice")
        return redirect(f"/play/{room_code}?&choice={char_choice}")
    return render(request, "index.html")
