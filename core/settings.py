from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    pay_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str('BOT_TOKEN'),
            pay_token=env.str('PAY_TOKEN'),
            admin_id=env.int('ADMIN_ID')
        )
    )

settings = get_settings('input')