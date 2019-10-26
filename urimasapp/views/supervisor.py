from django.contrib import messages
from django.contrib.auth import login

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, UpdateView


from ..forms import SupervisorSchoolForm, SupervisorSignUpForm
from ..models import Mission, Supervisor, User



class SupervisorSignUpView(CreateView):
    model = User
    form_class = SupervisorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'supervisor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('login')






# class SupervisorSchoolView(UpdateView):
#     model = Supervisor
#     form_class = SupervisorSchoolForm
#     template_name = 'supervisor/renamed.html'
#     success_url = reverse_lazy('super_mission_list')
#
#     def get_object(self):
#         return self.request.user.supervisor
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Interests updated with success!')
#         return super().form_valid(form)



class MissionListView(ListView):
    model = Mission
    ordering = ('mission_purpose', )
    context_object_name = 'missions'
    template_name = 'supervisor/mission_list.html'



    def get_queryset(self):

        supervisor = self.request.user.supervisor
        supervisor_school = supervisor.school.values_list('pk', flat=True)

        queryset = Mission.objects.filter(school__in=supervisor_school)
        return queryset



def mission_details(request, mission_id):


    invitation = get_object_or_404(Mission, pk=mission_id)

    return render(request, 'supervisor/mission_details.html', {'invitation': invitation})



def change_status(request, mission_id):
    invitation = get_object_or_404(Mission, pk=mission_id)

    #querry fo approving mission
    Mission.objects.filter(pk=mission_id).update(status='Approved')
    messages.success(request, 'mission Approved successfully!.')

    return render(request, 'supervisor/mission_details.html', {'invitation': invitation})


def reject_mission(request, mission_id):
    reject = get_object_or_404(Mission, pk=mission_id)

    #querry fo Rejecting mission
    Mission.objects.filter(pk=mission_id).update(status='Rejected')
    messages.success(request, 'mission Rejected!.')

    return render(request, 'supervisor/mission_details.html', {'invitation': reject})











