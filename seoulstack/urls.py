from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import faq, guidelines, welcome
from story.views import frontpage, submit, newest, vote, story

urlpatterns = [
    # story
    path('', frontpage, name='frontpage'),
    path('submit/', submit, name='submit'),
    path('newest/', newest, name='newest'),
    path('s/<int:story_id>/vote/', vote, name='vote'),
    path('s/<int:story_id>/', story, name='story'),

    path('u/', include('userprofile.urls')),




    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    # pages
    path('faq/', faq, name='faq'),
    path('guidelines/', guidelines, name='guidelines'),
    path('welcome/', welcome, name='welcome'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
