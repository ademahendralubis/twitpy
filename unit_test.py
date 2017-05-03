from twitPy import TwitterPy
import unittest

class TestTwitterPy(unittest.TestCase):
    
    #test show_timeline but we wrong input the token, Return False 
    def test_show_timeline_false(self):
        twit = TwitterPy(consumer_key="aa",consumer_secret="aa",access_token="aa",access_token_secret="aa")
        self.assertFalse(twit.show_timeline())
    
    #we received the timeline correctly, Return True
    def test_show_timeline_true(self):
        twit = TwitterPy(consumer_key="Nnd1GdqMqeELO9H7uH0m0bee6",consumer_secret="7lvtxt1Av0985JbX8bVmc2xkRI7Z8cD1Pcebg04PvbsnGKWnzO",access_token="859718216943194112-xd1MxsrsvXg8zPJ3bsC3iOPvUdADxhr",access_token_secret="UMLyuudrx3abMIolVURLeAqEN9fDZqujrDuD4s0dpdU9o")
        self.assertTrue(twit.show_timeline())
    
    #test post tweet but we wrong input the token, Return False 
    def test_post_tweet_false_1(self):
        twit = TwitterPy(consumer_key="aa",consumer_secret="aa",access_token="aa",access_token_secret="aa")
        self.assertFalse(twit.post_tweet("tes"))
    
    #if the message duplicated from your old tweets, return False
    def test_post_tweet_false_2(self):
        twit = TwitterPy(consumer_key="Nnd1GdqMqeELO9H7uH0m0bee6",consumer_secret="7lvtxt1Av0985JbX8bVmc2xkRI7Z8cD1Pcebg04PvbsnGKWnzO",access_token="859718216943194112-xd1MxsrsvXg8zPJ3bsC3iOPvUdADxhr",access_token_secret="UMLyuudrx3abMIolVURLeAqEN9fDZqujrDuD4s0dpdU9o")
        self.assertFalse(twit.post_tweet("tes a"))
    
    #if the message only contains spaces, return False
    def test_post_tweet_false_3(self):
        twit = TwitterPy(consumer_key="Nnd1GdqMqeELO9H7uH0m0bee6",consumer_secret="7lvtxt1Av0985JbX8bVmc2xkRI7Z8cD1Pcebg04PvbsnGKWnzO",access_token="859718216943194112-xd1MxsrsvXg8zPJ3bsC3iOPvUdADxhr",access_token_secret="UMLyuudrx3abMIolVURLeAqEN9fDZqujrDuD4s0dpdU9o")
        self.assertFalse(twit.post_tweet("   "))
    
    #we successful posting a tweet, return True
    def test_post_tweet_false_4(self):
        twit = TwitterPy(consumer_key="Nnd1GdqMqeELO9H7uH0m0bee6",consumer_secret="7lvtxt1Av0985JbX8bVmc2xkRI7Z8cD1Pcebg04PvbsnGKWnzO",access_token="859718216943194112-xd1MxsrsvXg8zPJ3bsC3iOPvUdADxhr",access_token_secret="UMLyuudrx3abMIolVURLeAqEN9fDZqujrDuD4s0dpdU9o")
        self.assertTrue(twit.post_tweet("tes x"))
        

if __name__ == '__main__':
    unittest.main(exit=False)