import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

#nltk.download()
sia = SentimentIntensityAnalyzer()

data = pd.read_csv("covidvaccine_1.csv")
file = open("us_scores.txt","w")
k=0
alist = []
dates = []

"""
location = ["Hong Kong","Hongkong","hongkong","香港","hong kong", "HongKong", "HK", "hk","Kowloon",
"Kwai Tsing",
"Sai Kung",
"Sha Tin",
"Tai Po",
"Tsuen Wan",
"Tuen Mun",
"Yuen Long",
"Kowloon City",
"Kwun Tong",
"Sham Shui Po",
"Wong Tai Sin",
"Yau Tsim Mong",
"Wan Chai","九龍城","觀塘","黃大仙","油尖旺","區","離島","葵青","北","沙田","大埔","荃灣","屯門","元朗"]
"""
#location = ["India","india"]    #11835
location = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia",
           "Wyoming","USA",'America','america'] #42457

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
for i in data['user_location']:
    for j in location:
        try:
            if j in i:
                alist.append(k)
                file.write(data['date'][k])
                file.write("\t")
                file.write(str(sia.polarity_scores(data['text'][k])))
                file.write("\t")
                file.write(str(data['user_location'][k]))
                file.write("\n")
                break
            #    print(data['text'][k])
                #dates.append(data['date'][k])
        except:
            pass
    k+=1
print(len(alist))

#print(dates)