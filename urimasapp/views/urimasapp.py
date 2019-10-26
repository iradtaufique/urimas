from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from urimasapp.render import Render
from urimasapp.models import Mission, Supervisor, Category, Role, Department, Transport, School
from django.shortcuts import get_object_or_404



##########################view for printing mission as pdf #################
class Pdf(View):

    def get(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        params = {

            'invitation': mission,
            'request': request,

        }
        return Render.render('mission_pdf.html', params)



@login_required
def home(request):
    return render(request, 'home/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


##########################view for profile ####################################
def profile(request):
    return render(request, 'profile.html')


###############################view for adding category ####################
class AddCategory(CreateView):
    model = Category
    template_name = 'urimasapp/add.html'
    fields = {
        'name'
    }


###############################view for adding department ####################
class AddDepartment(CreateView):
    model = Department
    template_name = 'urimasapp/add.html'
    fields = {
        'name',
        'category'
    }


###############################view for adding role ####################
class AddRole(CreateView):
    model = Role
    template_name = 'urimasapp/add.html'
    fields = {
        'name',
        'category'
    }

###############################view for adding transport ####################
class AddTransport(CreateView):
    model = Transport
    template_name = 'urimasapp/add.html'
    fields = {
        'transport'
    }


###############################view for adding school ####################
class AddSchool(CreateView):
    model = School
    template_name = 'urimasapp/add.html'
    fields = {
        'name',
        'category'
    }