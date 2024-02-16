from TikTokApi  import TikTokApi
import time
import keyboard
import schedule
import random
api = TikTokApi.get_instance()
likePrev = 0
comPrev = 0
sharePrev = 0
def dropTNT(times):
    xValue = str(random.randrange(93,246, 1))
    zValue = str(random.randrange(3, 88, 1))
    command = "summon minecraft:tnt -" + xValue + " 190 -" + zValue + " {Fuse:127b}"
    for x in range(times):
        keyboard.press_and_release('/')
        time.sleep(0.05)
        keyboard.write(command)
        time.sleep(0.05)
        keyboard.press_and_release('enter')
        time.sleep(0.05)
    
def getStats():
    video = api.get_tiktok_by_id("7032610059301555457")
    likeCount = video['itemInfo']['itemStruct']['stats']['diggCount']
    commentCount = video['itemInfo']['itemStruct']['stats']['commentCount']
    shareCount = video['itemInfo']['itemStruct']['stats']['shareCount']
    global likePrev
    global comPrev
    global sharePrev
    if likePrev != likeCount:
        print("oldlike = "+ str(likePrev) + "  newLike = " + str(likeCount))
        dropTNT(5)
        likePrev = likeCount
    if comPrev != commentCount:
        print("oldcom = "+ str(comPrev) + "  newcom = " + str(commentCount))
        dropTNT(5)    
        comPrev = commentCount
    if sharePrev != shareCount:
        print("oldshare = "+ str(sharePrev) + "  newshare = " + str(shareCount))
        dropTNT(5)
        sharePrev = shareCount

schedule.every(1).seconds.do(getStats)

while True:
    schedule.run_pending()


