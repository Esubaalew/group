from django.shortcuts import render
from .models import Member
from django.views import generic

def index(request):
    members = Member.objects.all()
    num_members = Member.objects.all().count()

    context = {
        "members": members,
        'numbers':num_members
    }

    return render(request,
                  'index.html',
                  context=context)
class MemberListView(generic.ListView):
    model = Member
    context_object_name = 'member_list'