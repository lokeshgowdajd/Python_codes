import requests

url = 'https://www.compress2go.com/result#j=d927464b-dd00-4d5f-ae18-4c3e5ee1eb8b/automation-testing-interview-questions-1.zip'
response = requests.get(url)

with open('automation-testing-interview-questions-1.zip', 'wb') as file:
    file.write(response.content)
