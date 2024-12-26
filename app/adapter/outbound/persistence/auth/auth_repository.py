from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError

from prisma import Prisma


class AuthRepository:
    def __init__(self, prisma: Prisma, password_hasher: PasswordHasher):
        self.prisma = prisma
        self.password_hasher = password_hasher

    async def verify_hash(self, plain, hashed) -> bool:
        try:
            return self.password_hasher.verify(hashed, plain)
        except InvalidHashError:
            return False
        except VerifyMismatchError:
            return False

    def get_hash(self, password) -> str:
        return self.password_hasher.hash(password)
