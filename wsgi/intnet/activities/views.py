from django.shortcuts import render
from activities.models import Activity, Feature, FeatureOption


def view_activity(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    features = activity.feature_set.all()

    return render(request, 'activities/main.html', {'activity': activity, 'features': features})