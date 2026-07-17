from handlers.user import routers as user_routers
from handlers.admin import routers as admin_routers


routers = [
    *user_routers,
    *admin_routers,
]