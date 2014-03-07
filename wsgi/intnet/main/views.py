from django.shortcuts import render
from activities.models import Activity, CarouselImage


def main(request):
    carousel_activities = Activity.objects.order_by('-purchases')[:3]
    carousel_images = CarouselImage.objects.filter(id__in=carousel_activities)
    activities = Activity.objects.all()
    return render(request, 'main/main.html', {'activities': activities, 'carousel_images': carousel_images})
