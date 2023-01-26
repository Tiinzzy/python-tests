def getting_reversed_stars(num):
    for i in range(num):
        i = '*'
        stars = ' ' + i * (2*num - 1)
        all_stars.append(stars)
        num -= 1


def getting_new_arrangement(len):
    for i in range(len):
        new_arrangement.append(i)

    new_arrangement.reverse()


def display_stars_from_one_to_many(all_stars):
    all_stars = [all_stars[i] for i in new_arrangement]

    for i in all_stars:
        number = 20
        print(i.center(number, ' '))
        number -= number


if __name__ == '__main__':
    num = input('Enter a number: ')
    num = int(num)

    all_stars = []
    new_arrangement = []

    getting_reversed_stars(num)

    tota_length = len(all_stars)

    getting_new_arrangement(tota_length)

    display_stars_from_one_to_many(all_stars)
