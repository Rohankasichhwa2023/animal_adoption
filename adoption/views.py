# adoption/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AnimalAdoptionForm
from .models import Animal
from django.db.models import Q 

def adoption_form(request):
    if request.method == 'POST':
        form = AnimalAdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Animal instance but don't save it yet
            new_animal = form.save(commit=False)
            new_animal.image = form.cleaned_data['image']  # Set the image field
            new_animal.save()  # Save the Animal instance

            return redirect('animal_list')  # Redirect to the animal_list page

    else:
        form = AnimalAdoptionForm()

    return render(request, 'adoption/adoption_form.html', {'form': form})

def animal_list(request):
    query = request.GET.get('q')
    if query:
        animals = Animal.objects.filter(Q(name__icontains=query) | Q(species__icontains=query))
    else:
        animals = Animal.objects.all()
    return render(request, 'adoption/adoption_list.html', {'animals': animals, 'query': query})


def animal_edit(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AnimalAdoptionForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')

    else:
        form = AnimalAdoptionForm(instance=animal)

    return render(request, 'adoption/animal_edit.html', {'form': form, 'animal': animal})