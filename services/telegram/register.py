from aiogram import Dispatcher

from services.telegram.handlers import main


class TgRegister:
    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def register(self):
        self._register_handlers()
        self._register_middlewares()

    def _register_handlers(self):
        self.dp.include_routers(main.router)

    def _register_middlewares(self):
        ...
        # middleware = DataMiddleware(self.orm, scheduler)
        #
        # self.dp.callback_query.middleware(middleware)
        # self.dp.message.middleware(middleware)
        # self.dp.inline_query.middleware(middleware)
