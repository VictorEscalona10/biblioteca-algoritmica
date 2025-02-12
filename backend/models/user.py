from pydantic import BaseModel, EmailStr, field_validator
import re

# pip install pydantic
# pip install "pydantic[email]"

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('name', 'email', 'password')
    def not_empty(cls, value):
        if not value.strip():
            raise ValueError("Este campo no puede estar vacío.")
        return value

    @field_validator('password')
    def validate_password(cls, value):
        # Máximo de caracteres
        if len(value) > 20:
            raise ValueError("La contraseña no puede tener más de 20 caracteres.")

        # Al menos una mayúscula
        if not re.search(r'[A-Z]', value):
            raise ValueError("La contraseña debe contener al menos una mayúscula.")

        # Al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError("La contraseña debe contener al menos un carácter especial.")

        # Al menos un número
        if not re.search(r'[0-9]', value):
            raise ValueError("La contraseña debe contener al menos un número.")

        return value
    
