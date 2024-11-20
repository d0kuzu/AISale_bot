from environs import Env


class Environ:
    def __init__(self):
        env = Env()
        env.read_env(".env")
        self.bot_token = env.str("BOT_TOKEN")
        self.dev_mode = env.bool("DEV_MODE")

    # def psycopg_url(self):
    #     return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
    #
    # def asyncpg_url(self):
    #     return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"