from TikTokApi import TikTokApi
import time
import schedule
api = TikTokApi.get_instance()
results = 10

video = api.get_tiktok_by_id("7019633115710655746")

likeCount = video['itemInfo']['itemStruct']['stats']['diggCount']
commentCount = video['itemInfo']['itemStruct']['stats']['commentCount']
shareCount = video['itemInfo']['itemStruct']['stats']['shareCount']
##followCount = api.get_user("dijonmstrd")['userInfo']['stats']['followerCount'] 
def logStats():
    video = api.get_tiktok_by_id("7019633115710655746")
    global likeCount
    global commentCount
    global shareCount
    ##global followCount
    print("Day " + str(time.gmtime()[2]) + " Hour " + str(time.gmtime()[3]) + " done")

    with open("Likes.txt", "a") as myfile:
        myfile.write(str(video['itemInfo']['itemStruct']['stats']['diggCount'] - likeCount)+ "\n")

    with open("Comments.txt", "a") as myfile:
        myfile.write(str(video['itemInfo']['itemStruct']['stats']['commentCount'] - commentCount)+ "\n")

    with open("Shares.txt", "a") as myfile:
        myfile.write(str(video['itemInfo']['itemStruct']['stats']['shareCount'] - shareCount)+ "\n")

    ##with open("Follows.txt", "a") as myfile:
        ##myfile.write(str(api.get_user("dijonmstrd")['userInfo']['stats']['followerCount']  - followCount)+ "\n")

    with open("DatePerLine.txt", "a") as myfile:
        myfile.write("Day " + str(time.gmtime()[2]) + " Hour " + str(time.gmtime()[3]) + "\n")

    likeCount = video['itemInfo']['itemStruct']['stats']['diggCount']
    commentCount = video['itemInfo']['itemStruct']['stats']['commentCount']
    shareCount = video['itemInfo']['itemStruct']['stats']['shareCount']
    ##followCount = api.get_user("dijonmstrd")['userInfo']['stats']['followerCount']  

logStats()
schedule.every(1).hours.do(logStats)

while True:
    schedule.run_pending()