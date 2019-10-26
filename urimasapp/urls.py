from django.urls import path
from .views import urimasapp, member_staff, supervisor, authorizer

urlpatterns = [

    path('', member_staff.MissionListView.as_view(), name='mission_request'),
    path('home/', urimasapp.home, name='home'),
    path('signup/', urimasapp.signup, name='signup'),
    path('staff_member/', member_staff.MissionListView.as_view(), name='mission_request'),
    path('mission/add/', member_staff.MissionCreateView.as_view(), name='mission_add'),

    path('report/', member_staff.Make_Report.as_view(), name='report'),



    path('invitation/<int:mission_id>/', supervisor.mission_details, name='invitation'),
    path('supervisor/', supervisor.MissionListView.as_view(), name='super_mission_list'),

    path('authorizer/', authorizer.AuMissionListView.as_view(), name='author_mission_list'),



    path('approve/<int:mission_id>', supervisor.change_status, name='change_status'),
    path('authorize/<int:mission_id>', authorizer.authorize_mission, name='authorize_mission'),
    path('rejected/<int:mission_id>', supervisor.reject_mission, name='reject_mission'),
    path('ajax/load-schools/', member_staff.load_schools, name='ajax_load_schools'),
    path('ajax/load-departments/', member_staff.load_department, name='ajax_load_department'),
    path('ajax/load-roles/', member_staff.load_role, name='ajax_load_role'),
    path('render/pdf/<int:pk>/', urimasapp.Pdf.as_view(), name='pdf'),
    path('profile/', urimasapp.profile, name='profile'),



    path('addCategory/', urimasapp.AddCategory.as_view(), name="add_category"),
    path('addDepartment/', urimasapp.AddDepartment.as_view(), name="add_department"),
    path('addRole/', urimasapp.AddRole.as_view(), name="add_role"),
    path('addTransport/', urimasapp.AddTransport.as_view(), name="add_transport"),
    path('addschool/', urimasapp.AddSchool.as_view(), name="add_school"),


]


