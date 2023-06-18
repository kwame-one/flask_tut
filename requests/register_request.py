from pydantic import BaseModel, constr


class RegisterRequest(BaseModel):
    email = constr(strip_whitespace=True, min_length=1)
    password = constr(strip_whitespace=True, min_length=1)
    password_confirmation = constr(strip_whitespace=True, min_length=1)
