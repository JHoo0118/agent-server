from argon2 import PasswordHasher

from prisma import Prisma


class RefreshTokenRepository:
    def __init__(self, prisma: Prisma, password_hasher: PasswordHasher):
        self.prisma = prisma
        self.password_hasher = password_hasher

    def update_rt_hash(self, email: str, hashed_rt: str) -> None:
        with self.prisma.tx() as transaction:
            transaction.refreshtoken.upsert(
                where={"userEmail": email},
                data={
                    "create": {
                        "token": hashed_rt,
                        "userEmail": email,
                    },
                    "update": {
                        "token": hashed_rt,
                    },
                },
            )

            transaction.user.update(
                where={"email": email},
                data={"refreshToken": {"connect": {"userEmail": email}}},
            )
