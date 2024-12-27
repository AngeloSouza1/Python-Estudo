from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from .user_model import User

class Task(Document):
    task_id: UUID = Field(default_factory=uuid4)
    status: bool = Field(default=False)
    title: Indexed(str)
    description: Optional[str] = None  # Removido Indexed por eficiência
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)  # Nome corrigido
    owner: Link[User]

    def __repr__(self) -> str:
        return f'Task(title={self.title})'

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.task_id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Task):
            return self.task_id == other.task_id
        return False

    @before_event([Replace, Insert])
    def update_timestamp(self):
        """Update the `updated_at` field before saving or replacing."""
        self.updated_at = datetime.utcnow()
