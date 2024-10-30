import logging
import uuid
from typing import Optional
from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from app.domain.users import Users
from app.infrastructure.config import settings


log = logging.getLogger(__name__)


class UserManager(UUIDIDMixin, BaseUserManager[Users, uuid.UUID]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret


    async def on_after_register(self, user: Users, request: Optional[Request] = None):
        log.warning("User %r has registered.", user.id)


    async def on_after_forgot_password(
        self, user: Users, token: str, request: Optional[Request] = None
    ):
        log.warning("User %r has forgot their password. Reset token: %r". user.id, token)


    async def on_after_request_verify(
        self, user: Users, token: str, request: Optional[Request] = None
    ):
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)
 