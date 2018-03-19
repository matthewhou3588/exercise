
# https://guoruibiao.gitbooks.io/effective-python/content/shi_yong_none_he_wen_dang_shuo_ming_dong_tai_de_zh.html#

import json


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

def decode2(data, default=None):
    """Load JSON data from string.

    :param data: JSON data to be decoded.
    :param default: Value to return if decoding fails.
        Defaults to an empty dictionary.
    :return:
    """

    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode2('bad data')
foo['stuff'] = 5
bar = decode2('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)


# https://guoruibiao.gitbooks.io/effective-python/content/jin_qiang_diao_guan_jian_zi_can_shu.html

# keyword-only arguments, in python3
def safe_division_c(number, division, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / division
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division_c(1, 0, ignore_zero_division=True)
