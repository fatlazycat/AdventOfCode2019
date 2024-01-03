
lower_val = 382345
lower_val_adjusted = "388888"
upper_val = 843167
upper_val_adjusted = "799999"


def has_adjacent_same(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False


def valid_passwords(lower_v1, init_lower_v2, upper_v1):
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
                            if has_adjacent_same(password):
                                count += 1

    return count


__all__ = ['valid_passwords']
