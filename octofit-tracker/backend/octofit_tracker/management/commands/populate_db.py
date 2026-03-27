from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team='Marvel'),
            User(name='Steve Rogers', email='steve@marvel.com', team='Marvel'),
            User(name='Bruce Wayne', email='bruce@dc.com', team='DC'),
            User(name='Clark Kent', email='clark@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        from datetime import date
        Activity.objects.create(user='Tony Stark', activity_type='Run', duration=30, date=date.today())
        Activity.objects.create(user='Steve Rogers', activity_type='Swim', duration=45, date=date.today())
        Activity.objects.create(user='Bruce Wayne', activity_type='Bike', duration=60, date=date.today())
        Activity.objects.create(user='Clark Kent', activity_type='Yoga', duration=50, date=date.today())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(name='Morning Cardio', description='Cardio for all', difficulty='Easy')
        Workout.objects.create(name='Strength Training', description='Strength for all', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(user='Tony Stark', score=1000)
        Leaderboard.objects.create(user='Steve Rogers', score=900)
        Leaderboard.objects.create(user='Bruce Wayne', score=1100)
        Leaderboard.objects.create(user='Clark Kent', score=950)

        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email...'))
        # Create unique index on email using pymongo
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
