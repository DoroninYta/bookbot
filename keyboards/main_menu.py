from aiogram import F
from aiogram.types import BotCommand

from lexicon.lexicon import LEXICON

async def set_main_menu(bot : Bot):
    main_menu_commands= [
        BotCommand(command = command,
                    decription = descriprion)
        for command, descriprion in LEXICON_COMMANDS.item()]
    async bot.set_my_commands(main_menu_commands)