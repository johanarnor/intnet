from django.shortcuts import render
from activities.models import Activity, CarouselImage, DescriptionImage


def main(request):
    activities = Activity.objects.all()

    carousel_activities = Activity.objects.order_by('-purchases')[:3]
    carousel_images = CarouselImage.objects.filter(id__in=carousel_activities)

    description_images = []
    for activity in activities:
        description_images.append(activity.descriptionimage_set.all()[0].image.url)

    print description_images
    activities_images = zip(activities, description_images)

    return render(request, 'main/main.html', {'activities': activities, 'carousel_images': carousel_images,
                                              'activities_images': activities_images})
