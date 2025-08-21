from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='8349664256:AAFrBbJg_zJfLwSWRDDcuTaW8OE5DUvnQCk')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_handler1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup ( )
    keyboard.add("/Go")
    await message.answer("Привет я бот психолог выслушаю пойму сдам в дурку (возможно)перед началом я задам пару вопросов ладно? ",reply_markup=keyboard)

@dp.message_handler(commands='Go')
async def start_handler2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup ( )
    keyboard.add("да")
    keyboard.add("нет")
    await message.answer("первый вопрос часто ли вы общаетесь с людьми?",reply_markup=keyboard)



@dp.message_handler(lambda message: message.text in ["да","нет"])
async def start_handler3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup ( )
    keyboard.add("до")
    keyboard.add("нэт")
    choice = message.text
    if choice == "да":
        await message.answer("с вами все нормально",reply_markup=keyboard)
    
    elif choice == "нет":
        await message.answer("возможно вы замкнуты в себе и боитесь чье го то мнения в этом случае я совентую вам начать почаще говорить с людми начните с общения в интернете потом договоритесь встретиться с человеком если вы смогли встретиться отлично если нет тк вы боитесь неоправдать его/её ожидания сходите к психологу ",reply_markup=keyboard)


    await message.answer("HELLO")
@dp.message_handler(lambda message: message.text in ["до","нэт"])
async def start_handler4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup ( )
    keyboard.add("Да")
    keyboard.add("Нет")
    choice = message.text
    if choice == "до":
        await message.answer("sss",reply_markup=keyboard)
    
    elif choice == "нэт":
        await message.answer("zzz",reply_markup=keyboard)


executor.start_polling(dp, skip_updates=True)

