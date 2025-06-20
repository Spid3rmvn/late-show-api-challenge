from server1.app import create_app
from server1.models import db
from server1.models.user import User
from server1.models.guest import Guest
from server1.models.episode import Episode
from server1.models.appearance import Appearance
from datetime import date


def seed_database():
    app = create_app()

    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create users
        user1 = User(username='admin')
        user1.set_password('password123')

        user2 = User(username='testuser')
        user2.set_password('test123')

        db.session.add_all([user1, user2])

        # Create guests
        guests = [
            Guest(name='Jennifer Lawrence', occupation='Actress'),
            Guest(name='Elon Musk', occupation='Entrepreneur'),
            Guest(name='Taylor Swift', occupation='Musician'),
            Guest(name='Stephen King', occupation='Author'),
            Guest(name='Serena Williams', occupation='Tennis Player')
        ]

        db.session.add_all(guests)

        # Create episodes
        episodes = [
            Episode(date=date(2024, 1, 15), number=1001),
            Episode(date=date(2024, 1, 16), number=1002),
            Episode(date=date(2024, 1, 17), number=1003),
            Episode(date=date(2024, 1, 18), number=1004),
        ]

        db.session.add_all(episodes)
        db.session.commit()

        # Create appearances
        appearances = [
            Appearance(rating=5, guest_id=1, episode_id=1),
            Appearance(rating=4, guest_id=2, episode_id=1),
            Appearance(rating=5, guest_id=3, episode_id=2),
            Appearance(rating=3, guest_id=4, episode_id=3),
            Appearance(rating=4, guest_id=5, episode_id=4),
        ]

        db.session.add_all(appearances)
        db.session.commit()

        print("Database seeded successfully!")


if __name__ == '__main__':
    seed_database()