from unittest import TestCase, main
from tasks.task_3_conquest_campaign import ConquestCampaign


class TestConquestCampaign(TestCase):

    def test_conquest_campaign_1(self):
        self.assertEqual(ConquestCampaign(1, 1, 1, [1, 1]), 1)

    def test_conquest_campaign_2(self):
        self.assertEqual(ConquestCampaign(2, 2, 2, [1, 1, 2, 2]), 2)

    def test_conquest_campaign_3(self):
        self.assertEqual(ConquestCampaign(2, 2, 1, [1, 2]), 3)

    def test_conquest_campaign_4(self):
        self.assertEqual(ConquestCampaign(4, 3, 2, [2, 2, 3, 4]), 3)

    def test_conquest_campaign_5(self):
        self.assertEqual(ConquestCampaign(3, 4, 2, [2, 2, 4, 3]), 3)

    def test_conquest_campaign_6(self):
        self.assertEqual(ConquestCampaign(3, 4, 3, [2, 2, 2, 2, 3, 4]), 3)

    def test_conquest_campaign_7(self):
        self.assertEqual(ConquestCampaign(6, 5, 3, [1, 5, 4, 2, 5, 4]), 5)


if __name__ == '__main__':
    main()
