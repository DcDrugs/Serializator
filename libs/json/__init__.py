from .jsonencode import JsonEncode
# from .jsondecode import json_decode

def dump(obj):
    return JsonEncode().json_encode(obj)





# def load(obj):
#     pass json_decode(obj)