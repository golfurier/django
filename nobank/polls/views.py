from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Poll, Choice

# Create your views here.


def polls_list(request):
    """
    Renders the Poll
    :param request:
    :return:
    """
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)


def polls_detail(request, poll_id):
    """
    Render poll_detail.html
    :param request:
    :param poll_id:
    :return:
    """
    # poll = Poll.objects.get(id=poll_id)
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        print("YOU POSTED!!!!!!")

    if request.method == "GET":
        print("YOU get me")

    context = {'poll': poll}
    return render(request, 'polls/poll_detail.html', context)


def poll_vote(request, poll_id):
    choice_id = request.POST.get('choice')
    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        poll = choice.question
        choice.votes += 1
        choice.save()
        return render(request, 'polls/poll_results.html', {'poll': poll})
    return render(request, 'polls/poll_results.html', {'error': True})