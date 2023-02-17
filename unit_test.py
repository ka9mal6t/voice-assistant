import unittest
from voice_assistant import Assistant


class TestUM(unittest.TestCase):
    def setUp(self):
        self.ass = Assistant()

    def test_hello(self):
        self.assertEqual(self.ass.answer('приветики пятница'), 'hello')

    def test_weather(self):
        self.assertEqual(self.ass.answer('температура на улице пятница'), 'weather')
    def test_task_manager(self):
        self.assertEqual(self.ass.answer('задачи компьютера'), 'task_manager')

    def test_music(self):
        self.assertEqual(self.ass.answer('включи музыку'), 'music')

    def test_steam(self):
        self.assertEqual(self.ass.answer('стим'), 'steam')

    def test_telegram(self):
        self.assertEqual(self.ass.answer('телега'), 'telegram')

    def test_time(self):
        self.assertEqual(self.ass.answer('сколько сейчас времени'), 'time')


if __name__ == '__main__':
    unittest.main()

