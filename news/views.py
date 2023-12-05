from django.shortcuts import render, redirect
from news.models import News, Category
from news.forms import CreateCategoryForm, CreateNewsForm


def home(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'home.html', context)


def news_details(request, id):
    new = News.objects.get(id=id)
    context = {'new': new}
    return render(request, 'news_details.html', context)


def register_category(request):
    # se for POST nesta rota, cria um formulário com os dados do POST
    # e salva no banco de dados
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            # form.save() => também poderia salvar assim no BD
            Category.objects.create(**form.cleaned_data)
            return redirect('home-page')
    else:
        # se for GET nesta rota, cria um formulário em branco
        form = CreateCategoryForm()
        context = {"form": form}
        return render(request, 'categories_form.html', context)


def register_news(request):
    # método POST: cria um formulário com os dados do POST e salva no BD
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    # método GET: cria um formulário em branco
    else:
        form = CreateNewsForm()
        context = {"form": form}
        return render(request, 'news_form.html', context)
