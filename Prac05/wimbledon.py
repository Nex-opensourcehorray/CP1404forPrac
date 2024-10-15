"""
CP1404/CP5632 Practical
User dictionary and set to display the champions.
"""

FILENAME = 'wimbledon.csv'
champions = []
countries = []
champions_for_win = {}


def main():
    read_from_csv()
    get_champion_count(champions)
    print("Wimbledon Champions:")
    for name in champions_for_win:
        print(f"{name} {champions_for_win[name]}")
    print()
    common_countries = organize_countries(countries)
    print(f"These {len(common_countries)} countries have won Wimbledon:")
    print(f"{common_countries}")


def read_from_csv():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            contexts = line.split(',')
            champion = ''.join(contexts[2])
            champions.append(champion)
            country = ''.join(contexts[1])
            countries.append(country)
    champions.pop(0)
    countries.pop(0)
    return champions, countries


def get_champion_count(champions):
    for champion in champions:
        if champion in champions_for_win:
            champions_for_win[champion] += 1
        else:
            champions_for_win[champion] = 1
    return champions_for_win


def organize_countries(countries):
    common_countries = []
    [common_countries.append(x) for x in countries if x not in common_countries]

    return common_countries


if __name__ == '__main__':
    main()
