from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from urimasapp.models import User, Mission, Report, Supervisor, School, Department, Role
from urimasapp.forms import StaffSignUpForm, MissionForm
from django.contrib.auth.decorators import login_required




class StaffSignUpView(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        return redirect('login')



@method_decorator(login_required, name='dispatch')
class MissionListView(ListView):
    model = Mission
    ordering = ('mission_purpose', )
    # pending = Mission.objects.filter(status='Pending').count()
    context_object_name = 'missions'
    template_name = 'urimasapp/staff_mission_list.html'


    def get_queryset(self):
        queryset = self.request.user.missions \
            .select_related('school') \

        return queryset




###############################view for requesting Mission ##########################################################
class MissionCreateView(CreateView):
    model = Mission
    form_class = MissionForm

    template_name = 'urimasapp/mission_add_form.html'

    def form_valid(self, form):
        mission = form.save(commit=False)
        mission.owner = self.request.user
        mission.save()
        messages.success(self.request, 'Mission requested successfully!.')
        return redirect('mission_request')


###############################view for loading schools Based on category ###########################################
def load_schools(request):
    category_id = request.GET.get('category')
    schools = School.objects.filter(category_id=category_id).order_by('name')

    return render(request, 'urimasapp/dropdown.html', {'schools': schools})


###############################view for loading department Based on category ###########################################
def load_department(request):
    category_id = request.GET.get('category')
    department = Department.objects.filter(category_id=category_id).order_by('name')

    return render(request, 'urimasapp/dropdown.html', {'departments': department})



###############################view for loading roles Based on category ###########################################
def load_role(request):
    category_id = request.GET.get('category')
    role = Role.objects.filter(category_id=category_id).order_by('name')

    return render(request, 'urimasapp/dropdown.html', {'roles': role})



###############################view for making report ##########################################################
class Make_Report(CreateView):
    model = Report
    fields = (

        'file',
        'note')
    template_name = 'urimasapp/report.html'


    def form_valid(self, form):
        report = form.save(commit=False)
        report.owner = self.request.user
        report.save()
        messages.success(self.request, 'Report Has been Sent Successfully.')
        return redirect('mission_request')


def PendingView(request):
    pending = Mission.objects.filter(status='Pending').count()
    context = {
        'pending': pending
    }
    template_name = 'base.html'

    return render(request, template_name, context)
