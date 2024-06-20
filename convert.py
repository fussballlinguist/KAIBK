'''
A script to anonymize JSON output files of Telegram export and instaloader,
written by https://github.com/Henning-arround
'''

import hashlib
import json

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

def anonymize_insta(data):
    for item in data:
        # Anonymize id and username within owner element
        item['owner']['id'] = hash_string(item['owner']['id'])
        item['owner']['username'] = hash_string(item['owner']['username'])
        # Anonymize id and username within answers
        for answer in item.get('answers', []):
            answer['owner']['id'] = hash_string(answer['owner']['id'])
            answer['owner']['username'] = hash_string(answer['owner']['username'])
    return data


def convert_insta(input, output):
       
    with open(input, 'r') as file:
        data = json.load(file)

    anonymized_data = anonymize_insta(data)

    with open(output, 'w') as file:
        json.dump(anonymized_data, file, indent=4)


def anonymize_telegram(data):
    for message in data['messages']:
        message['from'] = hash_string(message['from'])
        message['from_id'] = hash_string(message['from_id'])
    return data


def convert_telegram(input, output):
     
    with open(input, 'r') as file:
        data = json.load(file)

    anonymized_data = anonymize_telegram(data)

    with open(output, 'w') as file:
        json.dump(anonymized_data, file, indent=4)

convert_insta("instagram_comments.json", "anonymized_instagram_comments.json")
convert_telegram("telegram.json", "anonymized_telegram.json")


