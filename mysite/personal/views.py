from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'about.html')


def pages(request, full_slug):
    slugs = full_slug.split('/')
    template = 'base.html'

    if slugs:
        print slugs[-1]
        try:
            template = '%s.html' % slugs[-1]
            loader.get_template(template_name=template)
        except:
            template = 'base.html'
    else:
        template = 'index.html'

    return render(request, template)