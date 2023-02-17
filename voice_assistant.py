import speech_recognition
import os
import requests
from bs4 import BeautifulSoup
import pyttsx3
# import json
from datetime import datetime
from threading import Thread


class Assistant:
    def __init__(self):
        """constructor initial"""
        self._sr = speech_recognition.Recognizer()
        self._sr.pause_threshold = 0.5
        # with open(r"dict\commands.json") as file:
        #     self._commandList = json.load(file)
        self._commandList = {
            "commands": {
                "hello": [
                    "привет"
                ],
                "time": [
                    "врем"
                ],
                "task_manager": [
                    "задач"
                ],
                "music": [
                    "spotify",
                    "музык",
                    "спотифай"
                ],
                "weather": [
                    "погод",
                    "температур"
                ],
                "shutdown": [
                    "выключ"
                ],
                "reboot": [
                    "перезагруз"
                ],
                "steam": [
                    "steam",
                    "стим"
                ],
                "telegram": [
                    "telegram",
                    "телег"
                ],
                "discord": [
                    "discord",
                    "дискор"
                ],
                "epic_games": [
                    "epic",
                    "эпик",
                    "епик"
                ],
                "battle_net": [
                    "батл",
                    "battle"
                ],
                "chrome": [
                    "браузер",
                    "поисковик",
                    "chrome",
                    "google",
                    "гугл",
                    "хром"
                ],
                "speed_test": [
                    "скорост"
                ],
                "pycharm": [
                    "пайчарм",
                    "печар"
                ],
                "vscode": [
                    "vs",
                    "visual"
                ],
                "calc": [
                    "посчита",
                    "калькулятор"
                ]
            }
        }
        self._ready = False
        self._animation = False

    def get_commands(self):
        return self._commandList['commands'].keys()

    def __str__(self):
        """to String"""
        print(f'<object of Assistant>')

    def _start(self):
        self._animation = True

        def _animation_bar():
            i = 0
            while self._animation:
                if i == 0:
                    print('Ready . . . . . ', end='\r')
                    i += 1
                elif i == 1:
                    print('Ready  . . . . .', end='\r')
                    i = 0
                # time.sleep(0.01)
        t = Thread(target=_animation_bar)
        t.start()
        ask = self._listen()
        self._animation = False
        if ask.find('пятница ') >= 0:
            ask = ask.split('пятница ')[-1]
            self._answer(ask)
            if self._ready:
                self._start()
        else:
            pass
            if self._ready:
                self._start()

    def start(self):
        self._ready = True
        self._start()

    def _listen(self):
        """listens to speech and translates into a line"""
        try:
            with speech_recognition.Microphone() as mic:
                self._sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = self._sr.listen(source=mic)
                query = self._sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            return query
        except speech_recognition.UnknownValueError:
            return 'Не поняла, повторите еще раз!'

    @staticmethod
    def _find_keywords(self, string: str):
        # array of words
        array = string.split()
        # delete words shorter than 5 letters
        for word in array:
            if len(word) < 4:
                array.remove(word)
        # keyword search
        for word in array[::-1]:
            for key, keyList in self._commandList['commands'].items():
                for keyWord in keyList:
                    if word.startswith(keyWord):
                        return key
        return

    @staticmethod
    def _speak(speech: str):
        tts = pyttsx3.init()
        EN_VOICE_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20DSK"
        RU_VOICE_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Anna"
        tts.setProperty('voice', RU_VOICE_ID)
        tts.say(speech)
        tts.runAndWait()
        return

    @staticmethod
    def _commands(key: str):

        def _hello():
            Assistant._speak('Здраствуйте!')
            return

        def _task_manager():
            Assistant._speak('Открываю диспетчер задач!')
            _action = lambda: os.system('taskmgr')
            th = Thread(target=_action)
            th.start()
            return

        def _music():
            Assistant._speak('Открываю приложение МУЗЫКА!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\Spotify.lnk')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Произошла ошибка!')
            return

        def _steam():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\Steam.lnk')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _telegram():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\Telegram.lnk')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _discord():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\Discord.lnk')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _epic_games():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\"Epic Games Launcher.lnk"')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _battle_net():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\Battle.net.lnk')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _chrome():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\"Google Chrome.lnk"')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _speed_test():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\Speedtest.lnk')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _pycharm():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\"PyCharm Community Edition 2022.3"')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _vscode():
            Assistant._speak('Открываю приложение!')
            try:
                _action = lambda: os.system(r'C:\Users\yourb\"3D Objects"\Ярлыки\"Visual Studio Code"')
                th = Thread(target=_action)
                th.start()
            except:
                Assistant._speak('Извините, не удалось открыть приложение!')
            return

        def _weather():
            try:
                req = requests.get("https://sinoptik.ua/погода-одесса/")
                src = req.text
                soup = BeautifulSoup(src, "lxml")
                temperature = soup.find(class_="today-temp").text
                weather_temperature = soup.find(class_="today-time").find_next_sibling().find("img").get("alt")
                Assistant._speak(f"Температура: {temperature}")
                Assistant._speak(weather_temperature)
            except requests.exceptions.ConnectionError:
                Assistant._speak("Простите, не удалось выполнить запрос. Проверьте подключение.")
            return

        def _shutdown():
            Assistant._speak('Выключаю систему!')
            os.system(r'shutdown /s /t 0')
            return

        def _reboot():
            Assistant._speak('Перезагружаю систему!')
            os.system(r'shutdown /r /t 0')
            return

        def _time():
            now = datetime.now()
            Assistant._speak(f'{now.hour}:{now.minute}')
            return

        def _calc():
            Assistant._speak('Говорите что посчитать!')
            ass = Assistant()
            array = ass._listen()
            array = array.split()
            if len(array) == 3 and array[1] in ['+', '-', 'x', '/']:
                res = None
                if array[1] == '+':
                    res = int(array[0]) + int(array[2])
                elif array[1] == '-':
                    res = int(array[0]) - int(array[2])
                elif array[1] == 'x':
                    res = int(array[0]) * int(array[2])
                else:
                    res = int(array[0]) / int(array[2])
                if res is None:
                    Assistant._speak('Простите, я Вас не понимаю!')
                else:
                    Assistant._speak(res)
            else:
                Assistant._speak('Простите, я Вас не понимаю!')
            return

        # print(f'>{key}')
        exec(f'_{key}()')
        return

    def _answer(self, ask: str):
        """prepares a response to a string"""
        key = self._find_keywords(self, ask)
        if key:
            res = exec(f'self._commands(key)')
            return key
        else:
            Assistant._speak('Команда не найдена!')
