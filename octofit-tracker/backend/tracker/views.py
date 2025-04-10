from django.http import JsonResponse

def users_view(request):
    return JsonResponse({"message": "Users endpoint"})

def teams_view(request):
    return JsonResponse({"message": "Teams endpoint"})

def activity_view(request):
    return JsonResponse({"message": "Activity endpoint"})

def leaderboard_view(request):
    return JsonResponse({"message": "Leaderboard endpoint"})

def workouts_view(request):
    return JsonResponse({"message": "Workouts endpoint"})

def api_root(request):
    return JsonResponse({"message": "API Root"})
