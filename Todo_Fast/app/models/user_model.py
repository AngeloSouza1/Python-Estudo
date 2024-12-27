from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None  # Alterado para tipo booleano

    def __repr__(self) -> str:
        return f'User(email={self.email})'

    def __str__(self) -> str:
        return self.email

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @classmethod
    async def find_by_email(cls, email: str) -> Optional["User"]:  # Melhor nome do método
        """Find a user by email."""
        return await cls.find_one(cls.email == email)

    @property
    def created_at(self) -> datetime:
        """Get the creation timestamp if available."""
        # Certifique-se de que está funcionando como esperado no seu banco.
        return self.id.generation_time if hasattr(self.id, "generation_time") else None
