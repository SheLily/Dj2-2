from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()

counter_click['test'] = 0
counter_click['original'] = 0

counter_show['original'] = 0
counter_show['test'] = 0


def index(request):
    var = request.GET.get('from-landing')
    if var == 'original':
        counter_click['original'] += 1
    elif var == 'test':
        counter_click['test'] += 1

    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render(request, 'index.html')


def landing(request):
    var = request.GET.get('from-landing')
    if var == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    elif var == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')

    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render(request, 'landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    orig = counter_click['original'] / counter_show['orig inal'] if counter_show['orig inal'] else 0
    test = counter_click['test'] / counter_show['test'] if counter_show['test'] else 0
    return render(request, 'stats.html', context={
        'test_conversion': test,
        'original_conversion': orig,
    })
