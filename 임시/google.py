# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
from pymongo import MongoClient

client = MongoClient('mongodb+srv://mojito_maldives:cocktaillove@cluster0.yfcan.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbmojito


# emojis = [
#     {
#         'name': 'Grapes',
#         'value': '프루티',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/grapes_1f347.png'
#     },
#     {
#         'name':'Lemon',
#         'value': '아이셔',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/lemon_1f34b.png'
#     },
#     {
#         'name':'Hot Beverage',
#         'value': '아이써',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/hot-beverage_2615.png'
#     },
#     {
#         'name':'Droplet',
#         'value': '프레시',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/droplet_1f4a7.png'
#     },
#     {
#         'name':'Seedling',
#         'value': '허브',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/seedling_1f331.png'
#     },
#     {
#         'name':'Flag: United Kingdom',
#         'value': 'gin',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/flag-united-kingdom_1f1ec-1f1e7.png'
#     },
#     {
#         'name':'Cactus',
#         'value': 'tequila',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/cactus_1f335.png'
#     },
#     {
#         'name':'Desert Island',
#         'value': 'rum',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/desert-island_1f3dd-fe0f.png'
#     },
#     {
#         'name':'Snowman Without Snow',
#         'value': 'vodka',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/snowman-without-snow_26c4.png'
#     },
#     {
#         'name':'Tumbler Glass',
#         'value': 'whiskey',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/tumbler-glass_1f943.png'
#     },
#     {
#         'name':'Wine Glass',
#         'value': 'brandy',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/wine-glass_1f377.png'
#     },
#     {
#         'name':'Trophy',
#         'value': 'top100',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/trophy_1f3c6.png'
#     },
#     {
#         'name':'House with Garden',
#         'value': 'house-party',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/house-with-garden_1f3e1.png'
#     },
#     {
#         'name':'Sun',
#         'value': 'allseason-classics',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/sun_2600-fe0f.png'
#     },
#     {
#         'name':'Santa Claus: Light Skin Tone',
#         'value': 'christmas',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/santa-claus_light-skin-tone_1f385-1f3fb_1f3fb.png'
#     },
#     {
#         'name':'Clapper Board',
#         'value': 'movie-nights',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/clapper-board_1f3ac.png'
#     },
#     {
#         'name':'Fireworks',
#         'value': 'new-years-eve',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/fireworks_1f386.png'
#     },
#     {
#         'name':'Rainbow',
#         'value': 'downtown',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/rainbow_1f308.png'
#     },
#     {
#         'name':'Birthday Cake',
#         'value': 'birthday',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/birthday-cake_1f382.png'
#     },
#     {
#         'name':'Candle',
#         'value': 'time-for-you',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/candle_1f56f-fe0f.png'
#     },
#     {
#         'name':'Rose',
#         'value': 'valentines-day',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/rose_1f339.png'
#     },
#     {
#         'name':'Fire',
#         'value': 'anniversary',
#         'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/fire_1f525.png'
#     },
# ]



emojis = [
    # {
    #     'name':'Smiling Face with Smiling Eyes',
    #     'value':'booziness1',
    #     'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/smiling-face-with-smiling-eyes_1f60a.png'
    # },
    #  {
    #     'name':'Monkey Face',
    #     'value':'booziness3',
    #     'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/monkey-face_1f435.png'
    # },
    #  {
    #     'name':'Dog Face',
    #     'value':'booziness5',
    #     'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/dog-face_1f436.png'
    # },
    #  {
    #     'name':'Honey Pot',
    #     'value':'sweetness1',
    #     'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/honey-pot_1f36f.png'
    # },
    #  {
    #     'name':'Cigarette',
    #     'value':'sweetness5',
    #     'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/cigarette_1f6ac.png'
    # },
    {
        'name':'Red Question Mark',
        'value':'no info',
        'url':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/question-mark_2753.png'
    },
    ]
db.emoji.insert_many(emojis)
print(emojis)
print(1)


# n = 0
# while n < len(emojis):
#     db.emoji.insert_one(emojis[n])
#     print(emojis[n])
#     n = n + 1



# list(db.final_cocktail.aggregate([{"$group":{ "_id": "$name", "count": { "$sum": 1 } } }]))
# desc = list(db.D.find({}, {'_id': 1, 'howtomake': 1}))
# print(desc)
# howtomake = list(db.final_cocktail.distinct('howtomake'))
# print(howtomake[0])

# n = 0
# while n < 180:
#     doc = {
#         '_id' : n,
#         'howtomake' : howtomake[n] ,
#     }
#
#     print(doc)
#     db.D.insert_one(doc)
#     n = n + 1



# 셀레니움
# n = 0
# while n < 173:
#
#     n = desc[n]['_id']
#     d = desc[n]['howtomake']
#     print(n)
#
#     driver = webdriver.Chrome('/Users/suwanpark/Documents/CODE/selenium_prac/chromedriver')
#     driver.get("https://translate.google.co.kr/?hl=ko")
#     try:
#         # time.sleep(1)
#         element = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
#         element.send_keys(d)
#         time.sleep(3)
#         a = driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]")
#         print(a.text)
#
#         db.D.update_one({'_id':n},{'$set' : {"korean": a.text}})
#         n = n + 1
#
#     except:
#         print(n, '오류입니다.')
#         pass