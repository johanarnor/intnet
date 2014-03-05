from django.shortcuts import render
from activities.models import Activity

# Create your views here.


def main(request):

    activities = Activity.objects.all()
    return render(request, 'main/main.html', {'activities': activities})
