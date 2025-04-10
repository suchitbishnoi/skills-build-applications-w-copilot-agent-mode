from django.test import TestCase

class UsersTestCase(TestCase):
    def test_users_endpoint(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)

class TeamsTestCase(TestCase):
    def test_teams_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)

class ActivityTestCase(TestCase):
    def test_activity_endpoint(self):
        response = self.client.get("/api/activity/")
        self.assertEqual(response.status_code, 200)

class LeaderboardTestCase(TestCase):
    def test_leaderboard_endpoint(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, 200)

class WorkoutsTestCase(TestCase):
    def test_workouts_endpoint(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)
