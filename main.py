import os
import time
import random
import string
import requests

API = 'https://www.1secmail.com/api/v1/'
domian_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
domian = random.choice(domian_list)

def mail_generator():
    name_email = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name_email) for i in range(10))
    return username


def mail_read(mail=''):
    Api_Check_Box = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    get_txt = requests.get(Api_Check_Box).json()
    email_box = len(get_txt)
    if email_box == 0:
        print('[-] У вас нету сообщений ^_^ [проверка каждые 5 сек]')
    else:
        list_id = []
        for i in get_txt:
            for key, value in i.items():
                if key == "id":
                    list_id.append(value)
        print(f'[INFO] You have a {email_box} messages. You are email update 5 sek')

        current_dir = os.getcwd()
        final_dir = os.path.join(current_dir, 'all_email')

        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        for i in list_id:
            read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
            r = requests.get(read_msg).json()

            sender = r.get('from')
            subject = r.get('subject')
            date = r.get('data')
            content = r.get('textBody')

            mail_file_path = os.path.join(final_dir, f'{i}.txt')

            with open(mail_file_path, 'w') as file:
                file.write(f'{sender}\n, {subject}\n, {date}\n, {content}')



def mail_delete(mail=''):
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'deleteMailBox',
        'login': mail.split('@')[0],
        'domain': mail.split('@')[1]
    }
    r = requests.post(url, data=data)
    print(f'[X] You are {mail} is a delete')

def main():
    try:
        username = mail_generator()
        mail = f'{username}@{domian}'
        print('----------')
        print(f'[+] Ваш емеил адрес {mail}')
        print('----------')

        mail_requests = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

        while True:
            mail_read(mail=mail)
            time.sleep(5)

    except(KeyboardInterrupt):
        mail_delete(mail=mail)
        print('Программа прервана!!!')

if __name__ == '__main__':
    main()
