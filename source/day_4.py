
lower_val = 382345
lower_val_adjusted = "388888"
upper_val = 843167
upper_val_adjusted = "799999"


def has_adjacent_same(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False


def has_adjacent_same_but_not_more(arr):
    s = str(arr)
    return any(s[i] == s[i+1]
               and (i == 0 or s[i-1] != s[i])
               and (i == len(s) - 2
                    or s[i+2] != s[i]) for i in range(len(s) - 1))


def valid_passwords(lower_v1, init_lower_v2, upper_v1, func):
    count = 0

    for i1 in range(lower_v1, upper_v1+1):
        if i1 == 3:
            lower_v2 = init_lower_v2
        else:
            lower_v2 = i1

        for i2 in range(lower_v2, 10):
            for i3 in range(i2, 10):
                for i4 in range(i3, 10):
                    for i5 in range(i4, 10):
                        for i6 in range(i5, 10):
                            password = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
                            if func(password):
                                count += 1

    return count


__all__ = ['valid_passwords', 'has_adjacent_same', 'has_adjacent_same_but_not_more']
