def main():
    while True:
        fraction = input('Fraction:  ')
        try:
            convert_string(fraction)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        if convert_string(fraction) == 0.5:
            print('50%')
        elif convert_string(fraction) == 0.25:
            print('25%')
        elif convert_string(fraction) == 0.75:
            print('75%')
        elif convert_string(fraction) == 1:
            pass
        elif convert_string(fraction) == 0:
            pass


def convert_string(fraction):
    first_number = fraction.split('/')[0]
    second_number = fraction.split('/')[1]
    return int(first_number) / int(second_number)


main()