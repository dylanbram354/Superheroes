from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def details(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheroes/details.html', context)



def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability,
                                  secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def delete(request, id):
    hero = Superhero.objects.get(id=id)
    hero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))
    pass


def confirm_delete(request, id):
    hero = Superhero.objects.get(id=id)
    context = {
        'hero': hero
    }
    return render(request, 'superheroes/confirm_delete.html', context)


def edit(request, id):
    hero = Superhero.objects.get(id=id)
    context = {
        'hero': hero
    }
    if request.method == 'POST':
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary_ability')
        hero.secondary_ability = request.POST.get('secondary_ability')
        hero.catchphrase = request.POST.get('catchphrase')
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/edit.html', context)
    pass


