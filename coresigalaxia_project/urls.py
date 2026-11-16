from django.contrib import admin
from django.urls import include, path
from core import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cei-7-ani/', views.cei_7_ani, name='cei_7_ani'),
    path('traducerea-autorilor/', views.traducerea_autorilor, name='traducerea_autorilor'),
    path('lecturi-usoare/', views.lecturi_usoare, name='lecturi_usoare'),
    path('adevaruri-ascunse/', views.adevaruri_ascunse, name='adevaruri_ascunse'),
    path('cartea-saptamanii/', views.cartea_saptamanii, name='cartea_saptamanii'),
    path('proiecte-educativ-culturale/', views.proiecte_educativ_culturale, name='proiecte_educativ_culturale'),
    path('libraria-coresi/', views.libraria_coresi, name='libraria_coresi'),
    path('cine-a-fost-coresi/', views.cine_a_fost_coresi, name='cine_a_fost_coresi'),
    path('evaluare-manuscrise/', views.evaluare_manuscrise, name='evaluare_manuscrise'),
    path('vreau-sa-public/', views.vreau_sa_public, name='vreau_sa_public'),
    path('sa-vorbim-corect-romaneste/', views.sa_vorbim_corect_romaneste, name='sa_vorbim_corect_romaneste'),  
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('detalii-program/', views.detalii_program, name='detalii_program'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
