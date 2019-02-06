"""Django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as users_views
from library import views as library_views
from projects import views as pro_views
from polls import views as polls_views
from search import views as search_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/',include('chat.urls')),
    path('',include('blog.urls')),
    path('register/',users_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('profile/',users_views.profile,name='profile'),
    path('library/library-upload/',library_views.upload,name="library-upload"),
    path('library/books/',library_views.book_list,name="book_list"),
    path('library/books/upload',library_views.upload_book,name="upload_book"),
    path('projects/',pro_views.project_list,name="project_list"),
    path('projects/upload',pro_views.upload_project,name="upload_project"),
    path('project/star',pro_views.star_project,name='star_project'),
    path('project/<int:pk>/update/',pro_views.ProjectUpdateView.as_view(),name='update_project'),
    path('project/<int:pk>/delete/',pro_views.ProjectDeleteView.as_view(),name='delete_project'),
    path('polls/',polls_views.index,name="polls_index"),
    path('polls/create/',polls_views.create_poll,name="polls_create"),
    path('polls/<int:question_id>/',polls_views.detail,name="polls_details"),
    path('polls/<int:question_id>/results/',polls_views.results,name="polls_results"),
    path('polls/<int:question_id>/vote/',polls_views.vote,name="polls_vote"),
    path('polls/<int:question_id>/add/',polls_views.add_options,name="add_options"),
    path('search/',search_views.search,name='search'),
    path('contacts/',users_views.contact_list,name="contact_list")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
