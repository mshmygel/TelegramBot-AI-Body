import os

import requests

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiogram import F, Router

import app.keyboards as kb
from app.middlewares import TestMiddleware
from dotenv import load_dotenv
from config import TOGETHER_API_KEY


load_dotenv()

router = Router()
router.message.outer_middleware(TestMiddleware())


async def ask_ai(prompt: str) -> str:
    """Виконує запит до Together AI"""
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ API Error: {response.json().get('error', 'Unknown error')}"


class ChatAI(StatesGroup):
    waiting_for_prompt = State()

@router.message(F.text == "🧠 Ask AI Body")
async def ask_ai_start(message: Message, state: FSMContext):
    """Стартує очікування промпту для AI"""
    await state.set_state(ChatAI.waiting_for_prompt)
    await message.answer("💬 Введіть свій запит для AI:")

@router.message(ChatAI.waiting_for_prompt)
async def process_ai_request(message: Message, state: FSMContext):
    """Обробляє запит до Together AI"""
    user_prompt = message.text
    await state.clear()
    response = await ask_ai(user_prompt)
    await message.answer(response)


# class ChatGPT(StatesGroup):
#     waiting_for_prompt = State()
#
# async def ask_gpt(prompt: str) -> str:
#     print(f"API KEY: {API_KEY}")
#     client = openai.AsyncOpenAI(api_key=API_KEY)
#     response = await client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.8
#     )
#     return response.choices[0].message.content
#
# @router.message(F.text=="📊 Ask AI Body")
# async def ask_gpt_start(message: Message, state: FSMContext):
#     await state.set_state(ChatGPT.waiting_for_prompt)
#     await message.answer("Enter your GPT prompt")
#
# @router.message(ChatGPT.waiting_for_prompt)
# async def process_gpt_request(message: Message, state: FSMContext):
#     user_prompt = message.text
#     await state.clear()
#     response = await ask_gpt(user_prompt)
#     await message.answer(response)

class Registration(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        "Chose an option",
        reply_markup=kb.main
    )
    await message.reply(
        "Chose your next turn",
        reply_markup=kb.main_inline
    )
    await message.reply(
        f"Hi, \nyour ID is {message.from_user.id}\nName: {message.from_user.first_name}",
        reply_markup=kb.settings
    )

@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("This is the /help command.")

@router.message(F.text == "How are you?")
async def get_how_are_you(message: Message):
    await message.answer("OK!")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")

@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg",
        caption="You are sweety like a cat"
    )

@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("You chose catalog", show_alert=True)
    await callback.message.edit_text("Here you are! :)", reply_markup=await kb.inline_items())

@router.callback_query(F.data == "cart")
async def catalog(callback: CallbackQuery):
    await callback.answer("You chose cart", show_alert=True)
    await callback.message.answer("Your cart is empty...")

@router.callback_query(F.data == "contacts")
async def catalog(callback: CallbackQuery):
    await callback.answer("You chose contacts", show_alert=True)
    await callback.message.answer("You are contacting us.")

@router.message(F.text == "📝 Register")
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Registration.number)
    await message.answer(
        "⬇Please share your contact information by pressing the button below:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="📞 Share Contact", request_contact=True)]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

@router.message(Registration.number, F.contact)
async def reg_contact(message: Message, state: FSMContext):
    contact = message.contact
    if contact:
        await state.update_data(number=contact.phone_number)
        await state.clear()
        await message.answer(
            f"🎉Thank you, {contact.first_name}!\n✅Your phone number {contact.phone_number} has been saved.",
            reply_markup=kb.main
        )
    else:
        await message.answer("❌Something went wrong. Please try again.")



