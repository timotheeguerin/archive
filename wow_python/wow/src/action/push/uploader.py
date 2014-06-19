import requests
from getpass import getpass
from bs4 import BeautifulSoup


class Uploader:
    root_url = 'http://localhost:3000/'

    def upload(self, filename):
        print('pusshing')
        self.client = requests.session()
        print(filename)
        self.login()
        upload_url = self.url('/package/version/upload')
        token = self.get_authenticity_token(upload_url)
        files = {'file': open(filename, 'rb')}
        r = self.client.post(upload_url, files=files, headers={'X-CSRF-Token': token})
        json = r.json()
        if json['success']:
            print('Uploaded with success!')
        else:
            print('Error while uploading:')
            print(json['message'])

    def login(self):
        login_url = self.url('/users/sign_in')
        token = self.get_authenticity_token(login_url)
        while True:
            email = input('Email:')
            password = getpass('Password:')
            r = self.client.post(login_url,
                                 data={'user[email]': email, 'user[password]': password, 'return_json': True},
                                 headers={'X-CSRF-Token': token})
            if r.json()['success']:
                break
            else:
                print('Wrong credentials!')

    def url(self, extension):
        return self.root_url + extension

    def get_authenticity_token(self, url):
        r = self.client.get(url)
        soup = BeautifulSoup(r.text)
        return soup.find('meta', {'name': 'csrf-token'})['content']
