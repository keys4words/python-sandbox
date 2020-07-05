def main():
    try:
        raise ValueError('value is incorrect')
    except ValueError as e:
        print('Exception', e)
        raise

try:
    main()
except ValueError as e:
    print('ValueError detected')