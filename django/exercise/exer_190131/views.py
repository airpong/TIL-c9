from django.shortcuts import render,redirect
from .models import Movie

# Create your views here.
def movielist(request):
    movies=Movie.objects.all()
    return render(request,'movielist.html',{'movies':movies})
    
def newmovie(request):
    return render(request,'newmovie.html')
    
def createmovie(request):
    titleKr = request.POST.get('titleKr')
    titleEn = request.POST.get('titleEn')
    infoURL = request.POST.get('infoURL')
    score = request.POST.get('score')
    genre = request.POST.get('genre')
    summary = request.POST.get('summary')
    poster = request.FILES.get('poster')
    spectators = request.POST.get('spectators')
    picture1 = request.FILES.get('picture1')
    picture2 = request.FILES.get('picture2')
    picture3 = request.FILES.get('picture3')
    movie = Movie(titleKr=titleKr,spectators=spectators,titleEn=titleEn,infourl=infoURL,score=score,genre=genre,summary=summary,poster=poster,picture1=picture1,picture2=picture2,picture3=picture3)
    movie.save()
    return redirect('exer_190131:movielist')