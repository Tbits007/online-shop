from app.infrastructure.auth.dependencies.FastAPIUsersObject import fastapi_users


current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)
