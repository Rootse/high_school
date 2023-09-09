from unittest import TestCase, main
from tasks.task_9_the_rabbits_foot import TheRabbitsFoot


class TestTheRabbitsFoot(TestCase):

    def test_the_rabbits_foot_1(self):
        self.assertEqual(TheRabbitsFoot('отдай мою кроличью лапку', True), 'омоюу толл дюиа акчп йрьк')
        self.assertEqual(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False), 'отдаймоюкроличьюлапку')

    def test_the_rabbits_foot_2(self):
        self.assertEqual(TheRabbitsFoot('такс', True), 'тк ас')
        self.assertEqual(TheRabbitsFoot('тк ас', False), 'такс')

    def test_the_rabbits_foot_3(self):
        self.assertEqual(TheRabbitsFoot("я был сегодня в деревне.", True), "яеяе бгвв ыодн лдее снр.")
        self.assertEqual(TheRabbitsFoot("яеяе бгвв ыодн лдее снр.", False), "ябылсегоднявдеревне.")


if __name__ == '__main__':
    main()
