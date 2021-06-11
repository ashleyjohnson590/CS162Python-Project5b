#Author: Ashley Johnson
#Date: 4/22/2021
#Description: Program reads nobels.json file and user searches the data in nobels.json.
import json

class NobelData():
    """class reads nobels.json and searches it for the surnames of the winners of the category in the year.
    Returns a sorted list of surnames."""
    def __init__(self):

        data = None
        try:
            with open('nobels.json', 'r')as infile:
                data = json.load(infile)
        except FileNotFoundError:
            print("file not found")
        self._data = data["prizes"]

    def get_data(self):
        """gets data in nobels.json"""
        return self._data

    def search_nobel(self, year, category):
        """searches nobels.json for year and category and returns the surname of the winner."""
        data = self.get_data()
        nobel_list = []
        surname_list = []
        for entry in data:
            if entry['year']==year and entry['category']==category:
                nobel_list = entry['laureates']
                break
        for entry in nobel_list:
            print(entry)
            surname = entry["surname"]
            print(surname)
            surname_list.append(surname)
        return sorted(surname_list)
def main():
    nd = NobelData()
    data = nd.get_data()
    list = nd.search_nobel('2020', 'chemistry')
    print(list)

if __name__ == '__main__':
    main()
