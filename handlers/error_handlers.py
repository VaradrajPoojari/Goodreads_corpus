from starlette.responses import JSONResponse
from errors.errors import Endpoint5xxException


def load_error_handlers(app):
    @app.exception_handler(Endpoint5xxException)
    async def handler_500_exception(request, e: Endpoint5xxException):
        print(f'Unable to complete the request - received error: {e}')
        return JSONResponse(
            status_code=500,
            content={"message": f"Something went wrong with the request: {request} which triggered exception: {e}"},
        )