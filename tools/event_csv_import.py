import csv
from datetime import datetime


class EventDataImporter:

    @staticmethod
    def generate_dataset(filename="../data/Schedule-Grid view.csv", encoding="utf-8-sig"):
        reader = csv.reader(open(filename, 'r', encoding=encoding))

        columns = next(reader)

        data = []
        for line in reader:
            notes = line[0]

            if line[4] != '':
                notes += '\n' + line[4]

            if line[3] != '-':
                notes += "\nPercent Completed: " + line[3]

            if line[5] != '':
                notes += "\nMinutes Played: " + line[5]

            data.append({"game": line[1], "date": datetime.strptime(line[2], "%m/%d/%Y"), "notes": notes})
        return data


def main():
    data = EventDataImporter.generate_dataset()
    print(data)


if __name__ == "__main__":
    main()
