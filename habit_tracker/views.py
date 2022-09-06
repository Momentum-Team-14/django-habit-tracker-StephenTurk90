from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated:
        return redirect("habit")
    return render(request, "habit/home.html")


@login_required
def habit(request):
    sort_by = request.GET.get("sort") or "title"
    habit = Habit.objects.annotate(
        favorited=Exists(
            CustomUser.objects.filter(
                favorite_albums=OuterRef("pk"), pk=request.user.pk
            )
        )
    ).order_by(sort_by)
    return render(
        request, "music/list_albums.html", {"albums": albums, "sort_by": sort_by}
    )



class HabitForm:
    class Meta:
        model = Habit
        fields = ('title',)