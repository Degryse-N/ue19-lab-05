import requests

def main():

    url = 'https://official-joke-api.appspot.com/random_joke'

    response = requests.get(url)

    print(response.json()['setup'], response.json()['punchline'])


if __name__ == '__main__':
    main()
