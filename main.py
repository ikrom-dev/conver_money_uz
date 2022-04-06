import requests


def get_currency(code):
    url = "https://nbu.uz/uz/exchange-rates/json/"
    data = requests.get(url).json()
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        item = data[mid]
        if item.get('code') == code.upper():
            return item
        if item.get('code') > code.upper():
            high = mid - 1
        else:
            low = mid + 1
    return None


def convert(summa, code):
    data = get_currency(code)
    try:
        return summa * float(data.get('cb_price'))
    except AttributeError:
        return None


print(convert(1, '1'))
