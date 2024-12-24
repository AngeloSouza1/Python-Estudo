from pydantic import BaseModel, field_validator

class User(BaseModel):
    nome: str
    idade: int
    email: str

    # Atualizando para usar @field_validator no Pydantic 2
    @field_validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('E-mail está inválido')
        return value
    
    # Personalizando a saída
    def __str__(self):
        return f"Usuário: {self.nome}, Idade: {self.idade}, E-mail: {self.email}"

# Criando instâncias
user1 = User(
    nome='Fulano',
    idade=25,
    email='fulano@email.com'
)
user2 = User(
    nome='Sicrano',
    idade=21,
    email='sicrano@email.com'
)

# Exibindo as instâncias de forma amigável
print(user1)
print(user2)
