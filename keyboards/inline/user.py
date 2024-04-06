from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def user_like_button_def(likes, dislikes):
    user_like_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{likes} 👍", callback_data="like"),
                InlineKeyboardButton(text=f"{dislikes} 👎", callback_data="dislike"),
            ]
        ]
    )
    return user_like_button
