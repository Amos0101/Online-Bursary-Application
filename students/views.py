from .forms import FamilyBackgroundForm
from django.http import JsonResponse
from .models import SubCounty, County
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PersonalDetailsForm
from .models import SubCounty


# Define counties and their corresponding subcounties in a dictionary
COUNTIES_SUBCOUNTIES = {
    "Baringo": ["Baringo Central", "Baringo North", "Mogotio"],
    "Kitui": ["Kitui Central", "Kitui West", "Mwingi West"],
    "Nairobi": ["Westlands", "Lang'ata", "Kasarani", "Dagoretti", "Embakasi"],
    "Kisumu": ["Kisumu East", "Kisumu Central", "Nyando", "Kisumu West", "Muhoroni"],
    "Mombasa": ["Mvita", "Changamwe", "Kisauni", "Nyali"],
    "Nakuru": ["Nakuru Town East", "Nakuru Town West", "Rongai"],
    "Kiambu": ["Kiambu Town", "Thika Town", "Juja", "Ruiru"],
}
def student_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def homepage(request):
    return render(request, 'homepage.html')

def application(request):
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family')  # Redirect to next step
    else:
        form = PersonalDetailsForm()

    counties = list(COUNTIES_SUBCOUNTIES.keys())
    print("Counties being passed:", counties)  # Debugging line

    return render(request, 'application.html', {'form': form, 'counties': counties})


def get_subcounties(request, county_name):
    try:
        county = County.objects.get(name=county_name)  # Get county by name
        subcounties = SubCounty.objects.filter(county_id=county.id).values("id", "name")
        return JsonResponse({"subcounties": list(subcounties)})
    except County.DoesNotExist:
        return JsonResponse({"subcounties": []})  # Return empty if county not found


def family_background_view(request):
    if request.method == "POST":
        form = FamilyBackgroundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("")  # Redirect after successful submission
    else:
        form = FamilyBackgroundForm()

    return render(request, "family_background.html", {"form": form})

