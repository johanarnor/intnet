from django.shortcuts import render
from activities.models import Activity, Feature, FeatureOption, Price
from activities.forms import ActivityForm


def view_activity(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    features = activity.feature_set.all()
    prices = activity.price
    form = ActivityForm(features=features, activity=activity)

    return render(request, 'activities/main.html', {'activity': activity, 'features': features, 'prices': prices, 'form': form})