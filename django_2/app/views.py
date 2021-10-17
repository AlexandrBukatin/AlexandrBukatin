from django.shortcuts import render, HttpResponse
from functools import reduce
from django_2.ssss.helpers import include_static_content


# Create your views here.


def index(request):
    content = '<h1>Львов</h1><p> Город на западе Украины,' \
              ' центр Львовской области, Львовского района,' \
              ' Львовской общины, а также центр Львовской агломерации.' \
              ' Национально-культурный, образовательный и научный центр,' \
              ' крупный промышленный центр, а также большой транспортный узел,' \
              ' в печати называется столицей Галиции и Западной Украины.</p>'
    return HttpResponse(include_static_content(content))


def news(request):
    content = '<h1>Капітану легендарних «Карпат» виповнилося 80 років</h1><p>Сьогодні, 13 серпня,' \
              ' виповнюється 80 років одному з найвідоміших гравців «Карпат»,' \
              ' улюбленцю львівських та українських вболівальників Ігорю Євстаховичу Кульчицькому.</p>'
    return HttpResponse(include_static_content(content))


def management(request):
    content = '<h1>Міський голова Львова</h1><p>Андрій Садовий</p>'
    return HttpResponse(include_static_content(content))


def fact(request):
    content = '<h1>Факты</h1><p>С 1998 года Исторический центр Львова внесён в список' \
              ' Всемирного наследия ЮНЕСКО.' \
              ' В городе находится более чем 50 % памятников архитектуры Украины[5]. ' \
              'В 2009 году ему присвоено звание культурной столицы Украины[6]. ' \
              'Город периодически занимает ведущие места в рейтингах туристической ' \
              'и инвестиционной привлекательности[7][8][9]. В 2012 году был одним из четырёх городов Украины,' \
              ' принимавших чемпионат Европы по футболу «Евро — 2012». ' \
              'День города отмечают в 1-ю субботу мая.</p>'
    return HttpResponse(include_static_content(content))


def contact(request):
    content = '<h1>Экстренные телефоны Львова</h1>' \
              '<p>Горячая линия Львовского городского совета: 297-59-99<br>' \
              'Городская аварийная служба: 297-59-11</p>'
    return HttpResponse(include_static_content(content))


def history(request, city=None):
    cities = [
        {
            'name': 'people',
            'info': 'Франтишек Заремба (1751—1863 гг.) — солдат, участник восстания Костюшко .<br>'
                    'Кирилл Самвел Степанович (18.02.1755 — 8.12.1858 гг.) — архиепископ.<br>'
                    'Станислав Людкевич (24.01.1879 — 10.09.1979 гг.) — композитор, музыковед, фольклорист, педагог.'

        },
        {
            'name': 'photos',
            'info': ''
        }
    ]
    if not city:
        response = reduce(lambda acc, item: acc + f'<li><a href="/history/{item["name"]}">{item["name"]}</a></li>',
                          cities, '')
        content = '<h1>История</h1><p>Львов основан галицким князем' \
                  ' и королём Руси Даниилом Романовичем в середине XIII века[2][3],' \
                  ' предположительно, около 1256 года ' \
                  'становится столицей Галицко-Волынского княжества[4].</p>' \
                  f'<ul>{response}</ul>'
        return HttpResponse(include_static_content(content))

    result = None
    for c in cities:
        if c['name'].lower() == city.lower():
            result = c
            break
    content = f'<a href="/history"> Back! </a><h1>History: {result["name"]}</h1><p>{result["info"]}</p>'
    return HttpResponse(include_static_content(content))
