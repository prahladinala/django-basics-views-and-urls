from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
# urlpatters > list
# list item syntax > path('PATH/', FUNCTION TO RUN)

# FUNCTION THAT RETURNS SOME DATA
def projects(request):
    return HttpResponse('Here are our projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects"),
]

# GO TO URL http://localhost:8000/projects/
# As there is no home route/path so http://localhost:8000/ > return 404