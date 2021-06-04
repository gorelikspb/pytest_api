import requests

# Создание пользователя: POST /users
# {«username»: str, «password1»: str, «pasword2»: str}

# def print_request(r): #была нужна для отладки  
#   print (r.url)
#   print (r.json())

 
from time import time

#создается уникальное имя пользователя с использовнием unixtimestamp
#надеюсь тест не будет запускаться чаще раза в секунду, иначе потребуется другое решение)

url = 'http://bzteltestapi.pythonanywhere.com/'
unique_username = 'user' + str(int(time()))
pwd = 'password1'
other_pwd = 'password2'

unique_user =  {'username': unique_username, 
               'password1': pwd, 'password2': pwd}

def test_pwd_empty():
  pwd_empty = unique_user.copy()
  pwd_empty['password1'] = ''
  pwd_empty['password2'] = ''
  r = requests.post(url + 'users', json = pwd_empty) 
  assert r.json()['message'] == "Empty fields: ['password1', 'password2']"
  

def test_pwd_not_the_same():
  diff_pwd = unique_user.copy()
  diff_pwd['password2'] = other_pwd
  r = requests.post(url + 'users', json = diff_pwd) 
  assert r.json()['message'] == 'Passwords does not match'

def test_pwd_2long():
  long_pwd =unique_user.copy()
  long_pwd['password1'] = long_pwd['password1']*10
  long_pwd['password2'] = long_pwd['password1']
  r = requests.post(url + 'users', json = long_pwd) 
  assert r.json()['message'] == 'Password to long. Max length is 20 chars'

def test_create_user():
  r = requests.post(url + 'users', json = unique_user)
  assert r.json()['result'] == 'New user ' \
                            + unique_username \
                            +' successfully created'

def test_create_not_unique_user():
  doubled = unique_user.copy()
  doubled['username'] = unique_user['username']+'doubled'
  #not using previous test for not depending if it works
  r = requests.post(url + 'users', json = doubled) 
  #and again
  r = requests.post(url + 'users', json = doubled)
  assert r.json()['message'] == 'User Already exist'
  
def test_empty_name():
  empty_name = unique_user.copy()
  empty_name['username'] = ''

  r = requests.post(url + 'users', json = empty_name)
  assert r.json()['message'] == "Empty fields: ['username']"


def test_name_longer50():
  name_longer50 = unique_user.copy()
  name_longer50['username'] = unique_user['username']*5


# Обновление пароля пользвателя: PUT /users {
# «username»: str, «old_password»: str «password1»: str, «pasword2»: str}

old_pwd_user =  {'username': unique_username + 're', 
              'password1': pwd, 'password2': pwd}

renew_pwd =  {'username': unique_username +'re', 
               'old_password': pwd,
               'password1': other_pwd, 'password2': other_pwd}

def test_repwd_user_not_exist():
  r = requests.put(url + 'users', json = renew_pwd)
  assert r.json()['message'] ==  'User '+renew_pwd['username']+ ' not found'

def test_repwd():
  r = requests.post(url + 'users', json = old_pwd_user)
  r = requests.put(url + 'users', json = renew_pwd)
  assert r.json()['result'] ==  'Password successfully updated!'


todo = {'text': 'smth to do', 'status': 'TODO'}



unique_user_login =  {'username': unique_username, 
               'password': pwd}

def test_get_token():
  r = requests.post(url + 'login', json = unique_user_login)
  assert ('access_token') in r.json()


todo_creator =  {'username': unique_username + 'todo', 
               'password1': pwd, 'password2': pwd}

todo_login =  {'username': unique_username + 'todo', 
               'password': pwd}

def test_todo_creation():
  r = requests.post(url + 'users', json = todo_creator)
  r = requests.post(url + 'login', json =todo_login)
  token = r.json()['access_token']
  todo = {'text': 'smth to do', 'status': 'TODO'}
  headers = { 'Authorization' : 'Bearer ' + token }
  r = requests.post(url + 'todos/'+todo_login['username'], 
                    json = todo, headers=headers)

  assert r.json()['result'] ==  'New todo successfully created!'



