def get_level_stars(level):
    stars_count = 2 * level-1
    return '*' * stars_count


def get_level_space(max_level, level):
    return ' ' * (max_level-level)


if __name__ == '__main__':
    num = input('Enter a number: ')
    num = int(num)

    for i in range(1, num+1):
        print(get_level_space(num, i) + get_level_stars(i))


'''
1    *
2   ***
3  *****
4 *******
5*********
'''
