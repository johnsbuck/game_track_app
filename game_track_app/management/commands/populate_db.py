from django.core.management.base import BaseCommand
from game_track_app.models import *
from tools import generate_dataset


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "Default help string."

    def _create_consoles(self, data):
        console_set = set()
        for point in data:
            for con in point["Consoles"]:
                console_set.add(con)

        console_set.remove('')
        Console.objects.bulk_create([Console(name='')] + [Console(name=x) for x in console_set])

    def _create_series(self, data):
        series_set = set()

        for point in data:
            for series in point["Series"]:
                series_set.add(series)

        series_set.remove('')
        Series.objects.bulk_create([Series(name='')] + [Series(name=x) for x in series_set])

    def _create_genres(self, data):
        genre_set = set()
        for point in data:
            for genre in point["Genres"]:
                genre_set.add(genre)

        genre_set.remove('')
        Genre.objects.bulk_create([Genre(name='')] + [Genre(name=x) for x in genre_set])

    def _create_devs(self, data):
        dev_set = set()
        for point in data:
            for dev in point["Developers"]:
                dev_set.add(dev)

        dev_set.remove('')
        Developer.objects.bulk_create([Developer(name='')] + [Developer(name=x) for x in dev_set])

    def _create_games(self, data):
        for point in data:
            print("Game(name='" + point["Name"] + "')")
            temp = Game(name=point["Name"])
            temp.save()

            temp.consoles.add(*Console.objects.filter(name__in=point["Consoles"]))
            temp.genres.add(*Genre.objects.filter(name__in=point["Genres"]))
            temp.series.add(*Series.objects.filter(name__in=point["Series"]))
            temp.developers.add(*Developer.objects.filter(name__in=point["Developers"]))

            temp.save()

    def _create_user(self, data):
        user = User(name="John Bucknam")
        user.save()

    def _create_game_stats(self, data):
        owned = [x["Name"] for x in data if x["Owned"]]
        user = User.objects.get(name="John Bucknam")

        for point in data:
            if point["Owned"]:
                match point["Game Status"]:
                    case "Continuous":
                        temp = GameStat(status=GameStatEnum.CONTINUOUS)
                    case "In Progress":
                        temp = GameStat(status=GameStatEnum.IN_PROGRESS)
                    case "Finished Main Story":
                        temp = GameStat(status=GameStatEnum.FINISHED_MAIN_STORY)
                    case "Finished Main Story + Extra":
                        temp = GameStat(status=GameStatEnum.FINISHED_MAIN_STORY_PLUS)
                    case "Completed":
                        temp = GameStat(status=GameStatEnum.COMPLETED)
                    case "Dropped":
                        temp = GameStat(status=GameStatEnum.DROPPED)
                    case "Waitlisted":
                        temp = GameStat(status=GameStatEnum.WAITLISTED)
                    case "On Hold":
                        temp = GameStat(status=GameStatEnum.ON_HOLD)
                    case "Never Touching":
                        temp = GameStat(status=GameStatEnum.DROPPED)
                    case _:
                        temp = GameStat(status=GameStatEnum.NOT_PLANNED)

                print("GameStat(status=" + temp.status + ", game=" + point["Name"] + ")")
                temp.game = Game.objects.get(name=point["Name"])
                temp.user = user
                temp.save()

    def handle(self, *args, **options):
        data = generate_dataset(filename="data/Video Games-Master View.csv")

        print("------------------------")
        print("Create Developers")
        print("------------------------")
        self._create_devs(data)

        print("------------------------")
        print("Create Consoles")
        print("------------------------")
        self._create_consoles(data)

        print("------------------------")
        print("Create Series")
        print("------------------------")
        self._create_series(data)

        print("------------------------")
        print("Create Genres")
        print("------------------------")
        self._create_genres(data)

        print("------------------------")
        print("Create Games")
        print("------------------------")
        self._create_games(data)

        print("------------------------")
        print("Create User")
        print("------------------------")
        self._create_user(data)

        print("------------------------")
        print("Create Game Statuses")
        print("------------------------")
        self._create_game_stats(data)
