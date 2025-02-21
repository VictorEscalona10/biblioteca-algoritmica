from pydantic import BaseModel, field_validator
import re

class Book(BaseModel):
    title: str
    author: str
    category: str

    @field_validator('title', 'author', 'category')
    def not_empty(cls, value):
        if not value.strip():
            raise ValueError("Este campo no puede estar vacío.")
        return value
    
    @field_validator('author')
    def validate_author(cls, value):
        # No numeros
        if re.search(r'[0-9]', value):
            raise ValueError("Solo debe contener letras.")

        # No caracteres especiales
        if re.search(r'[!@#$%^&*(),?":{}|<>]', value):
            raise ValueError("El autor no debe tener caracteres especiales.")
        
        return value
    
    @field_validator('category')
    def validate_category(cls, value):
        # No numeros
        if re.search(r'[0-9]', value):
            raise ValueError("Solo debe contener letras.")

        # No caracteres especiales
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError("La categoria no debe tener caracteres especiales.")
        
        return value
