from fastapi import FastAPI, status

from schemas import PointsArray, MyResponse, Length, TestResponse
from utils import worker, create_array

app = FastAPI(
    debug=True,
    title="Test API",
    openapi_url="/openapi.json",
    redoc_url=None,
    docs_url="/docs",
)


@app.post(
    path="/evaluate-task/",
    status_code=status.HTTP_200_OK,
    name="Evaluate function params",
    response_model=MyResponse,
)
async def post(array: PointsArray):
    return worker(array)


@app.post(
    path="/evaluate-on-test-values/",
    status_code=status.HTTP_200_OK,
    name="Evaluate function params using test values",
    response_model=TestResponse,
)
async def post(length: Length):
    array = create_array(length=length.length)
    result = worker(array)
    return TestResponse(params=result, array=array)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app="main:app", reload=True)
