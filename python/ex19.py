name=input("enter your name ")
age=input("enter your age ")
fav_movies=input("enter youy favourouite movies and songs sep. by ,").split(',')
fav_song=input("enter your favourouite songs sep. by ,").split(',')
user={}
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_song

for key, value in user.items():
    print(f"{key}:{value}")
