import json
from pprint import pprint

import requests

BASE_URL = 'http://localhost:8000/api'


def create_user(chat_id):
    url = BASE_URL + '/users/'
    response = requests.get(url).text
    users = json.loads(response)
    user_exists = False
    for user in users:
        if user['chat_id'] == chat_id:
            user_exists = True
            break
    if not user_exists:
        data = {
            'chat_id': chat_id
        }
        requests.post(url, data=data)
    else:
        return 'User already exists'


def update_user(chat_id, full_name, phone_number):
    url = BASE_URL + '/users/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        if user['chat_id'] == chat_id:
            data = {
                'chat_id': chat_id,
                'full_name': full_name,
                'phone_number': phone_number
            }
            requests.put(url + f'{user["id"]}/', data=data)


def user_info(chat_id):
    url = BASE_URL + '/users/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        if user['chat_id'] == chat_id:
            return user['full_name']
    return None


def phone_info(chat_id):
    url = BASE_URL + '/users/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        if user['chat_id'] == chat_id:
            return user['phone_number']
    return None


def chat_id_info(chat_id):
    url = BASE_URL + '/users/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        if user['chat_id'] == chat_id:
            return user['chat_id']
    return None


def level_category():
    url = BASE_URL + '/levels/'
    response = requests.get(url).text
    levels = json.loads(response)
    return levels


def get_trial_video():
    url = BASE_URL + '/trial-videos/'
    response = requests.get(url).text
    videos = json.loads(response)
    return videos


def trial_video_update(id, file_id):
    url = BASE_URL + '/trial-videos/'
    response = requests.get(url).text
    videos_data = json.loads(response)
    for video in videos_data:
        if video['id'] == id:
            if video['video_file_id'] is None:
                video['video_file_id'] = file_id
            else:
                pass
            data = {
                'lesson_name': video['lesson_name'],
                'video_file_id': file_id
            }
            requests.put(url + f'{video["id"]}/', data=data)


def get_trial_video_by_name(id, level_name, lesson_name, file_id):
    url = BASE_URL + '/trial-videos/'
    response = requests.get(url).text
    videos = json.loads(response)
    for video in videos:
        if video['level'] == level_name and video['lesson_name'] == lesson_name:
            if video['id'] == id:
                if video['video_file_id'] is None:
                    video['video_file_id'] = file_id
                else:
                    pass
                data = {
                    'lesson_name': video['lesson_name'],
                    'video_file_id': file_id
                }
                requests.put(url + f'{video["id"]}/', data=data)


def get_questions():
    url = BASE_URL + '/questions/'
    response = requests.get(url).text
    questions = json.loads(response)
    return questions


def get_correct_option_id(id):
    url = BASE_URL + '/questions/'
    response = requests.get(url).text
    correct_option = json.loads(response)
    for question in correct_option:
        if question['id'] == id:
            question_title = question['title']
            question_id = question['id'] - 1
            answers = get_questions()[question_id]['answer']
            open_period = question['open_period']
            answer_list = []
            correct_option_id = []
            for answer in answers:
                answer_list.append(answer['answer'])
                if answer['is_correct']:
                    correct_option_id.append(answer['id'])
            x = 0
            if correct_option_id[0] <= 4:
                x = correct_option_id[0] - 1
            elif correct_option_id[0] % 4 == 0:
                x = correct_option_id[0] % 4 + 3
            elif correct_option_id[0] > 4:
                m = (correct_option_id[0] // 4) * 4
                x = (correct_option_id[0] % m) * (correct_option_id[0] // m) - 1
            data = {
                'question_id': question_id,
                'question_title': question_title,
                'correct_option': x,
                'open_period': open_period,
                'answer_list': answer_list
            }
            return data


def get_lesson_order():
    url = BASE_URL + '/lesson-order/'
    response = requests.get(url).text
    orders = json.loads(response)
    return orders


def get_existing_users():
    url = BASE_URL + '/existing-students/'
    response = requests.get(url).text
    users = json.loads(response)
    return users


def user_test():
    url = BASE_URL + '/tests/'
    response = requests.get(url).text
    tests = json.loads(response)
    return tests


def user_test_detail(id):
    url = BASE_URL + '/tests/'
    response = requests.get(url).text
    tests = json.loads(response)
    for test in tests:
        if test['id'] == id:
            level = test['level']
            test_name = test['lesson_name']
            title = test['test_title']
            link = test['test_link']

            data = {
                'level': level,
                'test_name': test_name,
                'title': title,
                'link': link
            }
            print(data)
            return data


def user_delete(chat_id):
    url = BASE_URL + '/users/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        if user['chat_id'] == chat_id:
            requests.delete(url + f'{user["id"]}/')
            break
