from twitPy import TwitterPy

consumer_key = "Nnd1GdqMqeELO9H7uH0m0bee6"
consumer_secret = "7lvtxt1Av0985JbX8bVmc2xkRI7Z8cD1Pcebg04PvbsnGKWnzO"
access_token = "859718216943194112-xd1MxsrsvXg8zPJ3bsC3iOPvUdADxhr"
access_token_secret = "UMLyuudrx3abMIolVURLeAqEN9fDZqujrDuD4s0dpdU9o"

twit = TwitterPy(consumer_key,consumer_secret,access_token,access_token_secret)

choose = ""

while(choose != "3"):
    print("Pilihan Menu\n===============\n")
    print("1.Show timeline \n2.Post a tweet\n3.Exit application")
    choose = input("masukkan pilihan: ")
    
    if choose == "1":
        twit.show_timeline()
        
    elif choose == "2":
        message = input("tulis pesan: ")
        twit.post_tweet(message)
        


