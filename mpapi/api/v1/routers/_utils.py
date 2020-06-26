from ._exceptions import mpapi_exceptions

def format_result(result: dict):
    if result['success'] is not True:
        raise mpapi_exceptions(result)
    return result['value']
