from django.test import TestCase

# Create your tests here.

#This is a simple exemple how a test working:
class TestExemple(TestCase):
    def test_limiting_moves(self):
        x = 10
        self.assertEqual(x, 10)

    def test_limiting_moves(self):
        redirect_to_game_completion_page = False
        total_allowed_plays = 9
        counter = 0

        while counter <= 9:
            #Player plays
            counter += 1
        
        self.assertEqual(counter, 10)

        
