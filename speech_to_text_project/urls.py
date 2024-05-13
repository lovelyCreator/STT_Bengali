"""speech_to_text_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from speech_to_text_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

# from django.urls import path
# from speech_to_text_app.views import transcribe_audio

# urlpatterns = [
#     path('', transcribe_audio, name='transcribe_audio'),
# ]
# from django.urls import path
# from speech_to_text_app.views import stream_transcription

# urlpatterns = [
#     path('stream-transcription/', stream_transcription, name='stream_transcription'),
# ]