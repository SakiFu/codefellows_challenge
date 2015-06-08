
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from saki.models import User


class IndexView(generic.ListView):
    template_name = 'saki/index.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
               return User.objects.filter(
                                       pub_date__lte=timezone.now()
                                       ).order_by('-pub_date')[:20]


class UserView(generic.ListView):
    template_name = 'saki/user.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        return User.objects.filter(
                                    pub_date__lte=timezone.now()
                                    ).order_by('-pub_date')[:20]





