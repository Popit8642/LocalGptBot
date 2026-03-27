from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime

router = Router()
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

import app.keyboard as kb
from app.generate import ask


class Generate(StatesGroup):
    generate_wait = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"""Hello, @{message.from_user.username}! This is a bot based on a local neural network. The bot is intended for personal use/functionality testing.""", reply_markup=kb.main)
    
@router.message(F.text == "About bot")
async def cmd_about(message: Message):
    await message.answer(f"This bot performs GPT functionality based on local neural network deployment. Model: llama3.2")

@router.message(F.text == "Start dialogue")
async def cmd_onegin_gpt(message: Message, state: FSMContext):
    await state.set_state(Generate.generate_wait)
    await message.answer("""You have entered GPT mode. To exit the mode, press the "Exit mode" button""", reply_markup=kb.cancel)

@router.message(Generate.generate_wait)
async def cmd_generate_response(message: Message, state: FSMContext):
    msg = await message.answer("📝LocalGPT is thinking...")
    await state.update_data(text_user=message.text)
    data = await state.get_data()
    print(f"{time_now} | [INFO] | @{message.from_user.username} - {data['text_user']}")
    response = ask(user_id=message.from_user.id, text=data['text_user'])
    await msg.delete()
    print(f"{time_now} | [INFO] | llama3.2 - {response}")
    await message.reply(f"{response}", reply_markup=kb.cancel)

@router.callback_query(F.data == 'cancel', Generate.generate_wait)
async def cancel_order(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.answer("You are out of the mode.")