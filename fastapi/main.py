from fastapi import APIRouter, FastAPI

app = FastAPI()

router = APIRouter()


@router.get("/hello")
async def hello(name: str):
    results = {"hello": name}

    return results


app.include_router(router, prefix="/api")
