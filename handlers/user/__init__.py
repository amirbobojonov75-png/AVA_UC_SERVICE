from .start import router as start_router
from .profile import router as profile_router
from .help import router as help_router
from .admin import router as admin_router
from .buy_uc import router as buy_uc_router
from .uc_select import router as uc_select_router
from .order import router as order_router
from .check import router as check_router
from .orders import router as orders_router


routers = [
    start_router,
    profile_router,
    help_router,
    admin_router,
    buy_uc_router,
    uc_select_router,
    order_router,
    check_router,
    orders_router,
]