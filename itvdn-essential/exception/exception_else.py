MAX_STARS = 30
WIDTH = 80


def print_result(number):
    if number == 0:
        stars_count = MAX_STARS
    else:
        stars_count = round(MAX_STARS / number)
    if stars_count > MAX_STARS:
        stars_count = MAX_STARS
    number_field_with = WIDTH - 2 * stars_count
    stars = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_with) + '}{0}'
    print(fmt.format(stars, number))

def divide_numbers():
    while True:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            result = first_number / second_number
            
        except (ValueError, ZeroDivisionError) as e:
            print('Error', e)
            print('Please try again')
            print()

        else:
            print_result(result)
            break

if __name__ == "__main__":
    divide_numbers()