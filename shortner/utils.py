import random
import string
from django.conf import settings

SHORTCODE_MAX = getattr(settings , "SHORTCODE_MAX", 15)
SHORTCODE_MIN = getattr(settings , "SHORTCODE_MIN", 6)


def code_generator(size= SHORTCODE_MIN, chars= string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance , size = SHORTCODE_MIN):
    new_code = code_generator(size=size)
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    UrlClass = instance.__class__
    sc_exists = UrlClass.objects.filter(shortcode=new_code).exists()
    if sc_exists:
        return create_shortcode(size=size)
    return new_code

