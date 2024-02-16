from TikTokApi  import TikTokApi
import time
import keyboard
import schedule
import random
api = TikTokApi.get_instance()
likePrev = 0
comPrev = 0
sharePrev = 0
def dropTNT():
    xValue = str(random.randrange(32,100, 1))
    zValue = str(random.randrange(0, 64, 1))
    command = "summon minecraft:tnt -" + xValue + " 40 -" + zValue + " {Fuse:127b}"
    keyboard.press_and_release('/')
    time.sleep(0.05)
    keyboard.write(command)
    time.sleep(0.05)
    keyboard.press_and_release('enter')

def getStats():
    video = api.get_tiktok_by_id("7015567244855905538")
    likeCount = video['itemInfo']['itemStruct']['stats']['diggCount']
    commentCount = video['itemInfo']['itemStruct']['stats']['commentCount']
    shareCount = video['itemInfo']['itemStruct']['stats']['shareCount']
    global likePrev
    global comPrev
    global sharePrev
    if likePrev != likeCount:
        print("oldlike = "+ str(likePrev) + "  newLike = " + str(likeCount))
        dropTNT()
        likePrev = likeCount
    if comPrev != commentCount:
        print("oldcom = "+ str(comPrev) + "  newcom = " + str(commentCount))
        dropTNT()    
        comPrev = commentCount
    if sharePrev != shareCount:
        print("oldshare = "+ str(sharePrev) + "  newshare = " + str(shareCount))
        dropTNT()
        sharePrev = shareCount

schedule.every(1).seconds.do(getStats)

while True:
    schedule.run_pending()
