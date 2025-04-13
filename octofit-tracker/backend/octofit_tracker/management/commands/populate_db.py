from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate and verify the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(_id=ObjectId(), username="john_doe", email="john@example.com", password="password")
        user2 = User.objects.create(_id=ObjectId(), username="jane_doe", email="jane@example.com", password="password")

        # Create Teams
        team1 = Team.objects.create(_id=ObjectId(), name="Team Alpha")
        team1.members.add(user1, user2)

        # Create Activities
        Activity.objects.create(_id=ObjectId(), user=user1, activity_type="Running", duration=timedelta(minutes=30))
        Activity.objects.create(_id=ObjectId(), user=user2, activity_type="Cycling", duration=timedelta(hours=1))

        # Create Leaderboard Entries
        Leaderboard.objects.create(_id=ObjectId(), user=user1, score=150)
        Leaderboard.objects.create(_id=ObjectId(), user=user2, score=200)

        # Create Workouts
        Workout.objects.create(_id=ObjectId(), name="Morning Run", description="A quick morning run to start the day")
        Workout.objects.create(_id=ObjectId(), name="Evening Yoga", description="Relaxing yoga session")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))

        # Verification logic
        self.stdout.write("\nVerifying database contents:\n")

        # Verify Users
        users = User.objects.all()
        self.stdout.write(f"Users: {list(users)}")

        # Verify Teams
        teams = Team.objects.all()
        self.stdout.write(f"Teams: {list(teams)}")

        # Verify Activities
        activities = Activity.objects.all()
        self.stdout.write(f"Activities: {list(activities)}")

        # Verify Leaderboard
        leaderboard = Leaderboard.objects.all()
        self.stdout.write(f"Leaderboard: {list(leaderboard)}")

        # Verify Workouts
        workouts = Workout.objects.all()
        self.stdout.write(f"Workouts: {list(workouts)}")
