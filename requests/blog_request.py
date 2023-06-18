from pydantic import BaseModel, constr


class BlogRequest(BaseModel):
    title: constr(strip_whitespace=True, min_length=1)
    content: constr(strip_whitespace=True, min_length=1)
