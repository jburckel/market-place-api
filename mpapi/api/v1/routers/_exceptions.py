from fastapi.exceptions import HTTPException

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
