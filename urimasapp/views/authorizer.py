from django.contrib import messages
from django.contrib.auth import login

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, UpdateView


from ..forms import AuthorizerSignUpForm
from ..models import Mission, Supervisor, User




class AuthorizerSignUpView(CreateView):
    model = User
    form_class = AuthorizerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'authorizer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('login')



class AuMissionListView(ListView):
    model = Mission
    ordering = ('mission_purpose', )
    context_object_name = 'approve'
    template_name = 'authorizer/author_mission_list.html'



    def get_queryset(self):

        supervisor = self.request.user.supervisor
        supervisor_school = supervisor.school.values_list('pk', flat=True)

        queryset = Mission.objects.filter(school__in=supervisor_school) \
            .filter(status='Approved')

        return queryset



def mission_details(request, mission_id):


    invitation = get_object_or_404(Mission, pk=mission_id)
    superv = get_object_or_404(Supervisor, pk=mission_id)
    return render(request, 'supervisor/mission_details.html', {'invitation': invitation, 'superv': superv})



def authorize_mission(request, mission_id):
    invitation = get_object_or_404(Mission, pk=mission_id)

    #querry fo authorizing mission
    Mission.objects.filter(pk=mission_id).update(status='Authorized')
    messages.success(request, 'mission Authorized successfully!.')

    return render(request, 'supervisor/mission_details.html', {'invitation': invitation})


# def reject_mission(request, mission_id):
#     reject = get_object_or_404(Mission, pk=mission_id)
#
#     #querry fo Rejecting mission
#     Mission.objects.filter(pk=mission_id).update(status='Rejected')
#     messages.success(request, 'mission Rejected!.')
#
#     return render(request, 'supervisor/mission_details.html', {'invitation': reject})

