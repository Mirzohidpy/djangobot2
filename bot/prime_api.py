import json
import requests

BASE_URL = 'http://localhost:8000/api'


def prime_videos_list():
    url = BASE_URL + '/prime-videos/'
    response = requests.get(url).text
    videos = json.loads(response)
    return videos


def prime_videos(video_id):
    url = BASE_URL + '/prime-videos/'
    response = requests.get(url).text
    videos = json.loads(response)
    for video in videos:
        video_level = video['level']
        video_teacher = video['teacher']
        video_lesson_name = video['lesson_name']
        video_url = video['video']
        video_file_id = video['video_file_id']
        id = video['id']
        if id == video_id:
            data = {
                'id': video_id,
                'video_level': video_level,
                'video_teacher': video_teacher,
                'video_lesson_name': video_lesson_name,
                'video_url': video_url[22:],
                'video_file_id': video_file_id,
                'video_id': video_id

            }
            return data


def existing_users():
    url = BASE_URL + '/existing-students/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        full_name = user['full_name']
        teacher = user['teacher']
        level = user['level']
        phone_number = user['phone_number']
        data = {
            'teacher': teacher,
            'level': level,
            'phone_number': phone_number,
            'full_name': full_name
        }
        print(data)
        return data


existing_users()


def prime_video_by_name(id, level_name, lesson_name, file_id):
    url = BASE_URL + '/prime-videos/'
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


def get_chat_id():
    url = BASE_URL + '/existing-students/'
    response = requests.get(url).text
    users = json.loads(response)
    return list(users)


def existing_user_chat_id(chat_id):
    url = BASE_URL + '/existing-students/'
    response = requests.get(url).text
    users = json.loads(response)
    for user in users:
        print(user)
        if user['chat_id'] is None:
            data = {
                'chat_id': chat_id,
                'full_name': user['full_name'],
                'phone_number': user['phone_number'],
            }
            requests.put(url + f'{user["id"]}/', data=data)


def prime_test():
    url = BASE_URL + '/prime-tests/'
    response = requests.get(url).text
    tests = json.loads(response)
    return tests


def prime_test_detail(id):
    url = BASE_URL + '/prime-tests/'
    response = requests.get(url).text
    tests = json.loads(response)
    for test in tests:
        if test['id'] == id:
            prime_level = test['level']
            prime_teacher = test['teacher']
            prime_test_name = test['lesson_name']
            prime_test_title = test['test_title']
            prime_test_link = test['test_link']

            data = {
                'prime_level': prime_level,
                'prime_teacher': prime_teacher,
                'prime_test_name': prime_test_name,
                'prime_test_title': prime_test_title,
                'prime_test_link': prime_test_link
            }
            print(data)
            return data
