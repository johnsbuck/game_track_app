import csv


class RecommendationDataImporter:

    @staticmethod
    def generate_dataset(filename="../data/Recommendations-Grid view.csv", encoding="utf-8-sig"):
        reader = csv.reader(open(filename, 'r', encoding=encoding))

        columns = next(reader)

        data = {}
        for line in reader:
            if line[0] not in data:
                data[line[0]] = []
            data[line[0]].append({"game": line[1], "notes": line[2]})

        return data


def main():
    data = RecommendationDataImporter.generate_dataset()
    print(data)


if __name__ == "__main__":
    main()
