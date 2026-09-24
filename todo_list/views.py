from django.shortcuts import get_object_or_404, redirect, render

from .models import List


def home(request):
    all_items = List.objects.all()
    context = {'all_items': all_items}
    return render(request, 'home.html', context)


def add(request):
    if request.method == 'POST':
        item_text = request.POST.get('item', '').strip()
        if item_text:
            List.objects.create(item=item_text, completed=False)
    return redirect('home')


def strike(request, item_id):
    item = get_object_or_404(List, id=item_id)
    item.completed = True
    item.save()
    return redirect('home')


def unstrike(request, item_id):
    item = get_object_or_404(List, id=item_id)
    item.completed = False
    item.save()
    return redirect('home')


def delete(request, item_id):
    item = get_object_or_404(List, id=item_id)
    item.delete()
    return redirect('home')


def about(request):
    context = {'myname': 'Bob'}
    return render(request, 'about.html', context)
