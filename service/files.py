from starlette.responses import StreamingResponse


def iter_file():
    with open("api/portfolio.json", mode="rb") as file_like:
        yield from file_like


def read_file():
    return StreamingResponse(iter_file(), media_type="application/json")