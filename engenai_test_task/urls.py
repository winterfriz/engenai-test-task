from django.contrib import admin
from django.urls import path, include

import documents
from users import views as user_views
from documents import views as documents_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', documents_views.document_list, name='document-list'),
    # TODO: move signup, login, logout into one group
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('documents/', include('documents.urls')),
]
