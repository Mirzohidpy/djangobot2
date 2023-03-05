import logging
import time
from pprint import pprint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, PollAnswer
from api import update_user, get_trial_video_by_name, phone_info, user_test, user_delete
from buttons import phone_number_btn, video_levels, test_levels, about_menu, versions_menu
from register_state import RegisterState
from api import create_user, user_info, get_lesson_order, get_trial_video, get_questions, get_existing_users, \
    get_correct_option_id
from buttons import main_menu
from prime_buttons import prime_menu
from prime_api import prime_videos, existing_users, prime_video_by_name, prime_videos_list, \
    existing_user_chat_id, prime_test_detail, prime_test, get_chat_id

BOT_TOKEN = '1215619594:AAFi0eM8_r70LdFKheNKn8PvJD4YEjYaFRQ'  # Bot token
ADMINS = [1019139151, ]  # adminlar ro'yxati
IP = 'localhost'  # Xosting ip manzili

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    create_user(chat_id=chat_id)
    i = 0
    user_status = user_info(chat_id=chat_id)
    prime_status = phone_info(chat_id=chat_id)
    print(prime_status)
    if not user_status:
        await message.answer(f"Assalomu alaykum, Welcome to <b>EngZone</b>.\n\n"
                             f"Click the /registration command to register.", parse_mode='html')
    elif prime_status:

        for user in get_existing_users():
            i += 1
            if user['phone_number'] == prime_status:
                existing_user_chat_id(chat_id=chat_id)
                await message.answer(f"Assalomu alaykum, Welcome to <b>EngZone</b>.\n\n"
                                     f"You are our prime student", parse_mode='html', reply_markup=prime_menu)
                break
            else:
                if i == 1:
                    await message.answer(f"Welcome to <b>EngZone</b>.", parse_mode='html', reply_markup=main_menu)


@dp.message_handler(commands=['registration'], state=None)
async def start_register(msg: Message):
    chat_id = msg.from_user.id
    user_status = user_info(chat_id=chat_id)
    if not user_status:
        await msg.answer("Enter your full name to register: ")
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def register_full_name(msg: Message, state: FSMContext):
    full_name = msg.text
    await state.update_data({'full_name': full_name})
    await msg.answer('Enter your phone number: ', reply_markup=phone_number_btn)
    await RegisterState.phone_number.set()


@dp.message_handler(content_types='contact', state=RegisterState.phone_number)
async def register_phone_number(msg: Message, state: FSMContext):
    chat_id = msg.from_user.id
    data = await state.get_data()
    full_name = data['full_name']
    phone_number = msg.contact.phone_number
    update_user(chat_id=chat_id, full_name=full_name, phone_number=phone_number)
    await state.finish()
    for user in get_existing_users():
        if user['phone_number'] == phone_number:
            update_user(chat_id=chat_id, full_name=full_name, phone_number=phone_number)
            await msg.answer('This phone number is already registered.', reply_markup=prime_menu)
            return
    await msg.answer("You are registered 😊😊😊 ✅", reply_markup=ReplyKeyboardRemove())
    await msg.answer(f"Welcome to <b>EngZone</b>.", parse_mode='html', reply_markup=main_menu)


@dp.message_handler(text='⬅Main menu')
async def main_btn_menu(msg: Message):
    await msg.answer(f"Main menu", reply_markup=main_menu)


@dp.message_handler(text="🎬Videos")
async def videos(msg: Message):
    await msg.answer("Choose a level of English", reply_markup=video_levels)


@dp.message_handler(text="⚖️Tests")
async def videos(msg: Message):
    await msg.answer("Choose a level of English", reply_markup=test_levels)


CHANNEL_ID = '-861778665'


@dp.message_handler(commands=['start_test'])
async def poll_test(msg: Message):
    await msg.answer("Test boshlandi")
    for question in get_questions():
        id = question['id']
        data = get_correct_option_id(id)
        correct_option_id = data['correct_option']
        question_title = data['question_title']
        open_period = data['open_period']
        answer_list = data['answer_list']
        global this_quiz
        this_quiz = await bot.send_poll(msg.chat.id, question_title,
                                        answer_list, type='quiz',
                                        correct_option_id=correct_option_id,
                                        is_anonymous=False, open_period=open_period)
        pprint(this_quiz)
        answer_list.clear()
        time.sleep(open_period)


@dp.poll_answer_handler()
async def poll_answer(quiz_answer: PollAnswer):
    print(quiz_answer)
    if this_quiz.poll.correct_option_id == quiz_answer.option_ids[0]:
        await bot.send_message(quiz_answer.user.id, 'Correct answer')
    else:
        await bot.send_message(quiz_answer.user.id, 'Wrong answer')


@dp.message_handler(text="⬅Back")
async def back_btn(msg: Message):
    await msg.answer(f"Videos", reply_markup=video_levels)


# @dp.message_handler(lambda message: message.text and 'tests' in message.text)
# async def beginner(message: Message):
#     for question in get_questions():
#         if message.text == question['level'] + ' tests':
#             await message.answer("To start your test click /start_test command")
#             break


@dp.message_handler(lambda message: message.text and 'videos' in message.text)
async def level_categories(msg: Message):
    lesson_order_btn = ReplyKeyboardMarkup(
        row_width=2,
    )
    for i in get_lesson_order():
        for level_name in get_trial_video():
            order_list = []
            if msg.text == level_name['level'] + ' videos':
                if i['lessonName'] == level_name['lesson_name']:
                    if i['lessonName'] not in order_list:
                        order_list.append(i['lessonName'])
                    for order in order_list:
                        lesson_order_btn.insert(KeyboardButton(text=order + " " + level_name['level']))
    lesson_order_btn.insert(KeyboardButton(text='⬅Back'))
    await msg.answer('Your videos list', reply_markup=lesson_order_btn)


@dp.message_handler(text="⬅Menu")
async def back_btn(msg: Message):
    await msg.answer(f"Main menu", reply_markup=prime_menu)


@dp.message_handler(text="📖About")
async def about(msg: Message):
    await msg.answer(f"About", reply_markup=about_menu)


@dp.message_handler(text="🗂Version")
async def versions(msg: Message):
    await msg.answer(f"Versions", reply_markup=versions_menu)


@dp.message_handler(text="⬅About")
async def back_about(msg: Message):
    await msg.answer(f"About", reply_markup=about_menu)


@dp.message_handler(lambda message: message.text and 'Prime' in message.text)
async def prime_function(message: Message):
    for user in get_existing_users():
        if message.from_user.id == user['chat_id']:
            print(user['chat_id'])
            if message.text == '🎬Videos Prime':
                level = user['level']
                print(level)
                if level:
                    prime_video_levels = ReplyKeyboardMarkup(
                        row_width=2,
                    )
                    prime_video_levels.insert(KeyboardButton(text=level + ' lessons'))
                    prime_video_levels.insert(KeyboardButton(text='⬅Menu'))
                    await message.answer(f"You currently enrolled to our {level} course, \n"
                                         f"For skipped lessons click the button below", reply_markup=prime_video_levels)

                else:
                    await message.answer(f"You are not our student yet")
            elif message.text == '⚖️Tests Prime':
                level = user['level']
                if level:
                    prime_test_levels = ReplyKeyboardMarkup(
                        row_width=2,
                    )
                    prime_test_levels.insert(KeyboardButton(text=level + ' premium tests'))
                    prime_test_levels.insert(KeyboardButton(text='⬅Menu'))
                    await message.answer(f"You currently enrolled to our {level} course, \n"
                                         f"For master lessons click the button below", reply_markup=prime_test_levels)


@dp.message_handler(lambda message: message.text and 'tests' in message.text)
async def prime_user_tests(message: Message):
    for user in get_existing_users():
        if message.from_user.id == user['chat_id']:
            lesson_number_btn = ReplyKeyboardMarkup(
                row_width=2,
            )
            if message.text == user['level'] + ' premium tests':
                for test in prime_test():
                    test_id = test['id']
                    test_data = prime_test_detail(test_id)
                    user_data = existing_users()
                    if user['level'] == test_data['prime_level'] and user['teacher'] == test_data[
                        'prime_teacher']:
                        lesson_number = test['lesson_name']

                        lesson_number_btn.insert(KeyboardButton(text=lesson_number + " test"))
                lesson_number_btn.insert(KeyboardButton(text='⬅Menu'))
                await message.answer(f"Your lessons list", reply_markup=lesson_number_btn)
            break

        else:
            lesson_number_btn = ReplyKeyboardMarkup(
                row_width=2,
            )

            for i in get_lesson_order():
                for level_name in user_test():
                    order_list = []
                    if message.text == level_name['level'] + ' tests':
                        if i['lessonName'] == level_name['lesson_name']:
                            if i['lessonName'] not in order_list:
                                order_list.append(i['lessonName'])
                            for order in order_list:
                                lesson_number_btn.insert(
                                    KeyboardButton(text=order + " test" + " " + level_name['level']))
            lesson_number_btn.insert(KeyboardButton(text='⬅Main menu'))
            await message.answer(f"Your lessons list", reply_markup=lesson_number_btn)
            break


@dp.message_handler(lambda message: message.text and 'test' in message.text)
async def prime_user_test(message: Message):
    for user in get_existing_users():
        if message.from_user.id == user['chat_id']:
            print(message.from_user.id)
            print(message.text)
            for test in prime_test():
                test_id = test['id']
                test_data = prime_test_detail(test_id)
                if user['level'] == test_data['prime_level'] and user['teacher'] == test_data[
                    'prime_teacher']:
                    lesson_number = test['lesson_name']
                    if message.text == lesson_number + ' test':
                        test_url = test_data['prime_test_link']
                        test = test_url
                        await message.answer(f"Your test is ready {test}")
        else:
            for level_name in user_test():
                exact_level = message.text.split()[2]
                if message.text == level_name['lesson_name'] + " test" + " " + exact_level:
                    if exact_level == level_name['level']:
                        test_url = level_name['test_link']
                        test = test_url
                        await message.answer(f"Your test is ready {test}")
            break
            # for level_name in get_trial_video():
            #     exact_level = msg.text.split()[1]
            #     if msg.text == level_name['lesson_name'] + " " + exact_level:
            #         if exact_level == level_name['level']:
            #             id = level_name['id']
            #             level_order_name = level_name['level']
            #             lesson_name = level_name['lesson_name']
            #
            #             video_url = level_name['video']
            #             file_id = level_name['video_file_id']
            #             video = video_url[22:]
            #             if file_id is None:
            #                 result = await bot.send_video(CHANNEL_ID, video=open(f'../{video}', 'rb'))
            #                 file_id = result['video']['file_id']
            #                 get_trial_video_by_name(id=id, file_id=file_id, level_name=level_order_name,
            #                                         lesson_name=lesson_name)
            #             else:
            #                 await bot.send_video(msg.from_user.id, video=file_id
            #             break


@dp.message_handler(lambda message: message.text and 'lessons' in message.text)
async def prime_lessons(message: Message):
    for user in get_existing_users():
        if message.from_user.id == user['chat_id']:
            lesson_number_btn = ReplyKeyboardMarkup(
                row_width=2,
            )
            if message.text == user['level'] + ' lessons':
                for video in prime_videos_list():
                    video_id = video['id']
                    video_data = prime_videos(video_id)
                    if user['level'] == video_data['video_level'] and user['teacher'] == video_data[
                        'video_teacher']:
                        lesson_number = video_data['video_lesson_name']

                        lesson_number_btn.insert(KeyboardButton(text=lesson_number + " premium"))
                lesson_number_btn.insert(KeyboardButton(text='⬅Menu'))
                await message.answer(f"Your lessons list", reply_markup=lesson_number_btn)


@dp.message_handler(lambda message: message.text and 'premium' in message.text)
async def prime_videos_function(message: Message):
    for user in get_existing_users():
        if message.from_user.id == user['chat_id']:
            print(message.from_user.id)
            user_data = existing_users()
            print(message.text)
            for video in prime_videos_list():
                video_id = video['id']
                video_data = prime_videos(video_id)
                if user['level'] == video_data['video_level'] and user['teacher'] == video_data[
                    'video_teacher']:
                    lesson_number = video_data['video_lesson_name']
                    if message.text == lesson_number + ' premium':
                        video_url = video_data['video_url']
                        file_id = video_data['video_file_id']
                        video = video_url
                        if file_id is None:
                            result = await bot.send_video(CHANNEL_ID, video=open(f'../{video}', 'rb'))
                            file_id = result['video']['file_id']
                            prime_video_by_name(id=video_data['id'], file_id=file_id,
                                                level_name=video_data['video_level'],
                                                lesson_name=video_data['video_lesson_name'])
                        else:
                            await bot.send_video(message.from_user.id, video=file_id)


@dp.message_handler()
async def level_categories(msg: Message):
    for level_name in get_trial_video():
        exact_level = msg.text.split()[1]
        if msg.text == level_name['lesson_name'] + " " + exact_level:
            if exact_level == level_name['level']:
                id = level_name['id']
                level_order_name = level_name['level']
                lesson_name = level_name['lesson_name']

                video_url = level_name['video']
                file_id = level_name['video_file_id']
                video = video_url[22:]
                if file_id is None:
                    result = await bot.send_video(CHANNEL_ID, video=open(f'../{video}', 'rb'))
                    file_id = result['video']['file_id']
                    get_trial_video_by_name(id=id, file_id=file_id, level_name=level_order_name,
                                            lesson_name=lesson_name)
                else:
                    await bot.send_video(msg.from_user.id, video=file_id)
                break


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
        ]
    )


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")

        except Exception as err:
            logging.exception(err)


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
