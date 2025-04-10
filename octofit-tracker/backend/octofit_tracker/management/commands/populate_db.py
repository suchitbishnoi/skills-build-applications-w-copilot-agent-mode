from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_users:
            User.objects.get_or_create(**user_data)

        # Populate teams
        for team_data in test_teams:
            Team.objects.get_or_create(**team_data)

        # Populate activities
        for activity_data in test_activities:
            Activity.objects.get_or_create(**activity_data)

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.get_or_create(**leaderboard_data)

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.get_or_create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
