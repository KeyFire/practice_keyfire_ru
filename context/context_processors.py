# coding: utf-8


def my_ip(request):
    """
    Отображает IP адрес посетителя
    :param request:
    :return:
    """
    return {'my_ip_address': request.META['REMOTE_ADDR']}
