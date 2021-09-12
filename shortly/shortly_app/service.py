
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def base63_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
    base36 = []
    while number != 0:
        number, i = divmod(number, 63)
        base36.append(alpha[i])
    return ''.join(reversed(base36))
