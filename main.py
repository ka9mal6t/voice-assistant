from voice_assistant import Assistant


def main():
    ass = Assistant()
    ass.start()


if __name__ == '__main__':
    main()



























    # import json
    # commandList = {'commands': {
    #             'hello': ['привет'],
    #
    #             'time': ['врем'],
    #
    #             'task_manager': ['задач'],
    #
    #             'music': ['spotify', 'музык', 'спотифай'],
    #
    #             'weather': ['погод', 'температур'],
    #
    #             'shutdown': ['выключ'],
    #
    #             'reboot': ['перезагруз'],
    #
    #             'steam': ['steam', 'стим'],
    #
    #             'telegram': ['telegram', 'телег'],
    #
    #             'discord': ['discord', 'дискор'],
    #
    #             'epic_games': ['epic', 'эпик', 'епик'],
    #
    #             'battle.net': ['батл', 'battle'],
    #
    #             'chrome': ['браузер', 'поисковик', 'chrome', 'google', 'гугл', 'хром'],
    #
    #             'speed_test': ['скорост'],
    #
    #             'pycharm': ['пайчарм', 'печар'],
    #
    #             'vdcode': ['vs', 'visual'],
    #
    #             'calc': ['посчита', 'калькулятор']
    #         }
    #         }
    # # #  ! Запись словаря в json файл
    # with open(r"dict/commands.json", "w") as file:
    #     json.dump(commandList, file, indent=4, ensure_ascii=False)
