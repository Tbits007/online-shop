from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTableUUID,
)

from app.infrastructure.database import Base


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):  
    pass