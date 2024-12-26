from prisma import Prisma
from prisma.models import User


class UserRepository:
    def __init__(self, prisma: Prisma):
        self.prisma = prisma

    async def get_user_by_email(self, email: str):
        return await self.prisma.user.find_unique(where={"email": email})

    async def create_user(
        self, email: str, hashed_password: str, username: str
    ) -> User:
        async with self.prisma.tx() as transaction:
            user: User = await transaction.user.create(
                {
                    "email": email,
                    "password": hashed_password,
                    "username": username,
                }
            )
            return user
