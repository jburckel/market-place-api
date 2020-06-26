from fastapi.exceptions import HTTPException

from mpapi.schemas.exceptions import Exceptions

def bad_request(detail: str = "Bad Request"):
    return HTTPException(
            status_code=400,
            detail=detail
        )

def not_found(detail: str = "Item not found"):
    return HTTPException(
            status_code=404,
            detail=detail
        )

def mpapi_exceptions(result: dict):
    error_id = result['error']
    if error_id == Exceptions.GET_NOT_FOUND:
        return not_found()
    elif error_id == Exceptions.GET_BAD_REQUEST:
        return bad_request()
    elif error_id == Exceptions.CREATE_BAD_REQUEST:
        return bad_request()
    elif error_id == Exceptions.UPDATE_BAD_REQUEST:
        return bad_request()
    elif error_id == Exceptions.DELETE_BAD_REQUEST:
        return bad_request()
    return HTTPException(
            status_code=404
        )
