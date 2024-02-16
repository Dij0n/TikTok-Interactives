from TikTokApi  import TikTokApi
import time
import keyboard
import schedule
api = TikTokApi.get_instance()
likePrev = 0
comPrev = 0
sharePrev = 0
def spawnAxo():
    command = "summon minecraft:axolotl 0 20 0"
    keyboard.press_and_release('/')
    time.sleep(0.05)
    keyboard.write(command)
    time.sleep(0.05)
    keyboard.press_and_release('enter')

def getStats():
    video = api.get_tiktok_by_id("7032266584131505410")
    likeCount = video['itemInfo']['itemStruct']['stats']['diggCount']
    commentCount = video['itemInfo']['itemStruct']['stats']['commentCount']
    shareCount = video['itemInfo']['itemStruct']['stats']['shareCount']
    global likePrev
    global comPrev
    global sharePrev
    if likePrev != likeCount:
        print("oldlike = "+ str(likePrev) + "  newLike = " + str(likeCount))
        spawnAxo()
        likePrev = likeCount
    if comPrev != commentCount:
        print("oldcom = "+ str(comPrev) + "  newcom = " + str(commentCount))
        spawnAxo()    
        comPrev = commentCount
    if sharePrev != shareCount:
        print("oldshare = "+ str(sharePrev) + "  newshare = " + str(shareCount))
        spawnAxo()
        sharePrev = shareCount

schedule.every(1).seconds.do(getStats)

while True:
    schedule.run_pending()



