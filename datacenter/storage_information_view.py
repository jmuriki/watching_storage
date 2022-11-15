from datacenter.models import Passcard, Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration, is_visit_long


def storage_information_view(request):
	active_visits = Visit.objects.filter(leaved_at=None)
	non_closed_visits = []
	for visit in active_visits:
		duration = get_duration(visit)
		formatted_duration = format_duration(duration)
		non_closed_visits.append(
			{
				'who_entered': visit.passcard,
				'entered_at': visit.entered_at,
				'duration': formatted_duration,
				'is_strange': is_visit_long(duration),
			}
		)
	context = {
		'non_closed_visits': non_closed_visits,
	}
	return render(request, 'storage_information.html', context)
