from prisma.models import User as UserEntity

from app.domain.user import User


class UserMapper:
    def __init__(self):
        pass

    @staticmethod
    def map_to_domain(user_entity: UserEntity) -> User:
        return User.generate_user(
            email=User.Email(user_entity.email),
            username=User.Username(user_entity.username),
            password=User.Password(user_entity.password),
            type=User.Type(user_entity.type),
            disabled=User.Disabled(user_entity.disabled),
            remain_count=User.RemainCount(user_entity.remainCount),
            created_at=User.CreatedAt(user_entity.createdAt),
            updated_at=User.UpdatedAt(user_entity.updatedAt),
            refreshToken=(
                User.RefreshToken(user_entity.refreshToken)
                if user_entity.refreshToken
                else None
            ),
        )
