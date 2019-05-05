from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, ContactForm
from django.template import loader


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = {
        'latest_poll_list': latest_poll_list,
    }
    return HttpResponse(t.render(c))


def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


def results(request, poll_id):
    return HttpResponse("results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form_is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()

        return render(request, 'contact.html', {
            'form': form,
        })
