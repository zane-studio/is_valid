name = "is_valid"

import re
import datetime


def is_email(value):
    """
    check if it is an Email string
    """
    pattern = "^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$"
    _reg = re.compile(pattern)
    result = re.match(_reg, value)
    return True if result is not None else False


def is_chinese_tel(value):
    """
    check if it is a chinese cell-phone number
    """
    pattern = "^1[345678]\d{9}$"
    _reg = re.compile(pattern)
    result = re.match(_reg, value)
    return True if result is not None else False


def is_chinese_card(value):
    """
    check if it is a 18-digit chinese ID card number
    """
    def _is_birth_valid(num):
        year = int(num[6:10])
        month = int(num[10:12])
        day = int(num[12:14])
        temp = datetime.datetime(year, month, day)
        return temp.year == year and temp.month == month and temp.day == day

    def _is_code_valid(num):
        wc = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
        valid_code_list = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        temp = [10 if i == 17 and v.lower() == 'x' else int(v) for i, v in enumerate(list(num))]
        code_sum = sum([temp[i] * wc[i] for i in range(len(temp) - 1)])
        return temp[17] == valid_code_list[code_sum % 11]

    if len(value) != 18:
        print("len not 18")
        return False

    if not value[:17].isdigit():
        print("not is digit")
        return False

    return _is_birth_valid(value) and _is_code_valid(value)


def is_visa_card(value):
    """
    check if it is a Visa card
    """
    pattern = "^4[0-9]{12}(?:[0-9]{3})?$"
    reg = re.compile(pattern)
    result = re.match(pattern, value)
    return True if result is not None else False


def is_master_card(value):
    """
    check if it is a Master card
    """
    pattern = "^5[1-5][0-9]{14}$"
    reg = re.compile(pattern)
    result = re.match(pattern, value)
    return True if result is not None else False


def is_link(value):
    """
    check if it is a link
    """
    pattern = "http(s)?\:\/\/([\w\d.?]+(\/)?)+"
    reg = re.compile(pattern)
    result = re.match(pattern, value)
    return True if result is not None else False


if __name__ == "__main__":
    # link
    value = "https://www.baidu.com"
    print(is_link(value))

