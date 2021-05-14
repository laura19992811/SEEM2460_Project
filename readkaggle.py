import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import emoji
import re
import xlsxwriter

def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    # tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
    #      if w.lower() in words or not w.isalpha())
    return tweet

def cleandate(date):
    date = date.split()[0]
    adate = [int(p) for p in date.split('-')]

    maxval = max(adate)
    if len(str(adate[1])) != 2:
        adate[1] = '0' + str(adate[1])
    if adate.index(maxval) == 2:  # 2021-02-05
        date = str(adate[2]) + "-" + str(adate[1]) + "-" + str(adate[0])
    else:
        date = str(adate[0]) + "-" + str(adate[1]) + "-" + str(adate[2])
    return date



#nltk.download()
sia = SentimentIntensityAnalyzer()

data = pd.read_csv("covidvaccine_1.csv")
workbook = xlsxwriter.Workbook('india_kaggle.xlsx')
worksheet = workbook.add_worksheet()
#file = open("hk_scores_kaggle.csv","w")
k=0
alist = []


#
# location = ["Hong Kong","Hongkong","hongkong","香港","hong kong", "HongKong", "HK", "hk","Kowloon",
# "Kwai Tsing",
# "Sai Kung",
# "Sha Tin",
# "Tai Po",
# "Tsuen Wan",
# "Tuen Mun",
# "Yuen Long",
# "Kowloon City",
# "Kwun Tong",
# "Sham Shui Po",
# "Wong Tai Sin",
# "Yau Tsim Mong",
# "Wan Chai","九龍城","觀塘","黃大仙","油尖旺","區","離島","葵青","北","沙田","大埔","荃灣","屯門","元朗"]
location = ["india","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry", "India"]
#location = ["India","india","Mumbai","Delhi]    #11835
# location = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia",
#            "Wyoming","USA",'America','america'] #42457
"""
location = ['Israel','israel',
"Afula","Akko","Arad","Ariel","Ashdod","Ashkelon","Baqa al-Gharbiyye","Bat Yam","Beer Sheva","Beit Shean",
 "Beit Shemesh","Betar Illit","Bnei Berak","Dimona","Eilat","Elad","Givatayim","Hadera","Haifa","Harish","Herzliya",
 "Hod HaSharon","Holon","Jerusalem","Karmiel","Kfar Sava","Kiryat Ata","Kiryat Bialik","Kiryat Gat","Kiryat Malachi",
 "Kiryat Motzkin","Kiryat Ono","Kiryat Shemone","Kiryat Yam","Lod","Maale Adumim","Maalot Tarshiha","Migdal HaEmek",
 "Modiin","Nahariya","Nazareth","Nes Ziona","Nesher","Netanya","Netivot","Nof Hagalil","Ofakim","Or Akiva","Or Yehuda",
 "Petah Tikva","Qalansawe","Raanana","Rahat","Ramat Hasharon","Ramat-Gan","Ramla","Rehovot","Rishon Lezion",
 "Rosh Ha'ayin","Sakhnin","Sderot","Shefaram","Taibeh","Tamra","Tel Aviv","Tiberias","Tira",
 "Tirat Carmel","Tsfat","Umm al-Fahm","Yavne","Yehud-Monosson","Yokneam"]
"""
#date, negative, neutral, positive, compound,location

rownum = 0
for i in data['user_location']:
    for j in location:
        try:
            if j in i:

                alist.append(k)
                date = data['date'][k]

                date = cleandate(date)

                tweet = cleaner(data['text'][k])

                scores = sia.polarity_scores(tweet)
                loc = data['user_location'][k]

                arow = [date,scores['neg'],scores['neu'],scores['pos'],scores['compound'],loc]
                for col_num, info in enumerate(arow):
                    worksheet.write(rownum, col_num, info)
                rownum+=1


                break

        except:
            pass
    k+=1
# df1 = pd.DataFrame(framerows,
#                    columns=['date', 'negative','positive','neutral','compound','location'])
workbook.close()
print(len(alist))

