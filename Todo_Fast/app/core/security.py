from passlib.context import CryptContext

password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

# Criptografia da senha
def get_password(password: str) -> str:
    return password_context.hash(password)

# Descriptografia da senha
def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)