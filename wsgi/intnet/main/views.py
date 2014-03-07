from django.shortcuts import render
from activities.models import Activity, CarouselImage


def main(request):
    activities = Activity.objects.all()

    carousel_activities = Activity.objects.order_by('-purchases')[:3]
    activity_ids = []
    for activity in carousel_activities:
        activity_ids.append(activity.pk)
    carousel_images = CarouselImage.objects.filter(activity__in=activity_ids).order_by('?')

    description_images = []
    for activity in activities:
        description_images.append(activity.descriptionimage_set.all()[0].image.url)

    activities_images = zip(activities, description_images)

    return render(request, 'main/main.html', {'carousel_images': carousel_images,
                                              'activities_images': activities_images})
