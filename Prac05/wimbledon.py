"""
CP1404/CP5632 Practical
User dictionary and set to display the champions.
"""

FILENAME = 'wimbledon.csv'
champions = []
countries = []
champions_for_count = {}


def main():
    """This function will do the printing."""
    read_from_csv()
    get_champion_count(champions)
    print("Wimbledon Champions:")
    for name in champions_for_count:
        print(f"{name} {champions_for_count[name]}")
    print()
    common_countries = organize_countries(countries)
    print(f"These {len(common_countries)} countries have won Wimbledon:")
    print(f"{common_countries}")


def read_from_csv():
    """This function allow you to read the csv and store it into two lists."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            contexts = line.split(',')
            champions.append(contexts[2])
            countries.append(contexts[1])
    champions.pop(0)
    countries.pop(0)
    return champions, countries


def get_champion_count(champions):
    """This function is to add the information to the dictionary."""
    for champion in champions:
        if champion in champions_for_count:
            champions_for_count[champion] += 1
        else:
            champions_for_count[champion] = 1
    return champions_for_count


def organize_countries(countries):
    """This function is to fetch the common countries to the other list."""
    """common_countries = []
    [common_countries.append(x) for x in countries if x not in common_countries]"""
    common_countries = set(countries)
    return common_countries


if __name__ == '__main__':
    main()
