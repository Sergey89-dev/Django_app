from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


links_menu =[
    {
        'url': 'products',
        'title': 'Все'
    },
    {
        'url': 'products_home',
        'title': 'Дом'

    },
    {
        'url': 'products_office',
        'title': 'ОФис'

    },
    {
        'url': 'products_modern',
        'title': 'модерн'

    },
    {
        'url': 'products_classic',
        'title': 'классика'

    }
]


def products(request):
    context = {
        'links_menu ': links_menu,
        'title': 'продукты'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_home(request):
    context = {
        'links_menu ': links_menu,
        'title': 'продукты для дома'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_office(request):
    context = {
        'links_menu ': links_menu,
        'title': 'продукты для оффиса'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_modern(request):
    context = {
        'links_menu ': links_menu,
        'title': 'продукты модерн'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_classic(request):
    context = {
        'links_menu ': links_menu,
        'title': 'продукты классика'
    }
    return render(request, 'mainapp/products.html', context=context)
