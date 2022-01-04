import csv


class GameDataImporter:

    def generate_dataset(self, filename="../data/Video Games-Master View.csv", encoding="utf-8-sig"):
        reader = csv.reader(open(filename, 'r', encoding=encoding))
        columns = next(reader)

        data = []
        for line in reader:
            data.append(self.generate_object(columns, line))

        return data

    def generate_object(self, columns, new_data):
        output = {x: y for x, y in zip(columns, new_data)}

        # Remove first half of Game Status string
        if len(output["Game Status"]) > 0:
            output["Game Status"] = output["Game Status"].split(" - ")[1]
        else:
            output["Game Status"] = output["Game Status"]

        # Split multiple listings
        if len(output["Consoles"]) > 0:
            output["Consoles"] = output["Consoles"].split(',')
        else:
            output["Consoles"] = [output["Consoles"]]

        if len(output["Developers"]) > 0:
            output["Developers"] = output["Developers"].split(',')
        else:
            output["Developers"] = [output["Developers"]]

        if len(output["Genres"]) > 0:
            output["Genres"] = output["Genres"].split(',')
        else:
            output["Genres"] = [output["Genres"]]

        if len(output["Series"]) > 0:
            output["Series"] = output["Series"].split(',')
        else:
            output["Series"] = [output["Series"]]

        # Set owned to true or false
        output["Owned"] = output["Owned"] == "checked"

        # Delete unnecessary columns
        del output["Calendar"]
        del output["Recommendations"]

        return output


def main():
    data = GameDataImporter.generate_dataset()


if __name__ == "__main__":
    main()
