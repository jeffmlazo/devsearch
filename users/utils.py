from django.db.models import Q
from .models import Profile, Skill


def searchProfiles(request):
    search_query = ''
    # Check if there is a value in the form
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)
    """
    This method will filter the search results for the search query if their is no match then return all the profiles with filter for name or short intro. This will also elminate duplicates using the distinct method.
    """
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    return profiles, search_query
