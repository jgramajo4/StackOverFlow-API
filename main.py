import json
import requests

response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

for questions in response.json()['items']:
  if questions['answer_count'] == 0:
    print(questions['title'])
    print(questions['link'])
  else:
    print('Skipped')
    print()
