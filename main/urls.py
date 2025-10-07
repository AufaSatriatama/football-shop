from django.urls import path
from main.views import show_main
from main.views import show_dashboard
from main.views import show_main, add_jersey, show_jersey, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_jersey
from main.views import delete_jersey
from main.views import register_ajax
from main.views import add_jersey_entry_ajax
from main.views import delete_jersey_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('dashboard/', show_dashboard, name='show_dashboard'),
    path('add-jersey/', add_jersey, name='add_jersey'),
    path('jersey/<str:id>/', show_jersey, name='show_jersey'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:jersey_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:jersey_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('register-ajax', register_ajax, name='register-ajax'),
    path('delete-jersey-ajax/<uuid:id>', delete_jersey_ajax, name='delete_jersey_ajax'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-jersey-entry-ajax', add_jersey_entry_ajax, name='add_jersey_entry_ajax'),
    path('jersey/<uuid:id>/edit', edit_jersey, name='edit_jersey'),
    path('jersey/<uuid:id>/delete', delete_jersey, name='delete_jersey'),
]