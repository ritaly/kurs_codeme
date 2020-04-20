import sys

list_elem = ['5', 'jeden', '4.5', 4, 0, ['xxx', 'yyy'], {1, 2, 3}, {'a': 1, 'b': 2}]

for i in list_elem:
    try:
        dzielenie = 10/int(i)
    except ZeroDivisionError:
        print('Zero')
    except TypeError:
        print('Type')
    # except ValueError:
    #     print('Value')
    except Exception:
        print(sys.exc_info()[0].__name__)
    else:
        print(dzielenie)

