from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🧠 Ask AI Body")],
    [KeyboardButton(text="📝 Register"),
     KeyboardButton(text="🌍 Send Location", request_location=True)],
],
    resize_keyboard=True,
    input_field_placeholder="Select menu item"
)

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Catalog", callback_data="catalog")],
    [InlineKeyboardButton(text="Cart", callback_data="cart"),
     InlineKeyboardButton(text="Contacts", callback_data="contacts")]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="💪Check Mike's GitHub",
        url="https://github.com/mshmygel"
    )],
    [InlineKeyboardButton(
        text="🤓View LinkedIn",
        url="https://www.linkedin.com/in/mike-shmygel/"
    )],
    [InlineKeyboardButton(
        text="🫡Open CV",
        url="https://drive.google.com/file/d/1BJlu-CoEwcLziWp9woFwlO-kxxAD_Ecj/view?usp=sharing"
    )],
])


items = ["item 1", "item 2", "item 3", "item 4"]

async def inline_items():
    keyboard = InlineKeyboardBuilder()
    for item in items:
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f"item_{item}"))
    return keyboard.adjust(2).as_markup()