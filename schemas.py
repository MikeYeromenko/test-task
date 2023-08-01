from typing import List

from pydantic import BaseModel, Field


class Length(BaseModel):
    length: int = Field(ge=1, le=101, default=100)


class Point(BaseModel):
    x: float
    y: float


class PointsArray(BaseModel):
    array: List[Point] = Field(min_items=2)


class MyResponse(BaseModel):
    a: float
    b: float
    c: float


class TestResponse(BaseModel):
    params: MyResponse
    array: PointsArray
