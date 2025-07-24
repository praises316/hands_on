# Task 1: Jos Food and Culture Festival Menu (Modified)
meals = ["Gwote", "Masa", "Tuwon Acha", "Fura da Nono", "Kunu", "Miyan Kuka"]

kunu  =  meals.insert(4,"Kunu")
print(meals)

meals.remove(meals[1])
print(meals)

meals.remove(meals[3])
print(meals)
meals.append("Fura da nono")
print(meals)

#2: Film Night Prep
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]
print(genres)
genres.append("Drama")
print(genres)
genres.remove(genres[3])
genres.remove(genres[5])
print(genres)

print(len(genres))

print(genres[1])
print(genres[-2])

newGenreList = genres
print(newGenreList)

# 3
money = [1000, 1200, 800, 1500, 1100]
sumOfMoney = sum(money)
print(sumOfMoney)

money[2] = 1000
print(money)

print(money[::-1])
# 4
courseList = ["MTH 101","PHY 101","CHM 101","CSC 101","GST 101"]
addCourse = courseList.insert(0,"ENG 101")
print(courseList)

removecourse =  courseList.remove(courseList[-1])
print(courseList)
addCourse = courseList.insert(3,"BIO 101")
print(courseList)

print(courseList[2])

friendsList = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
addKemi = friendsList.insert(4,"Kemi")
print(friendsList)

removeDaniel = friendsList.remove(friendsList[1])
print(friendsList)
friendsList[0] = "Aisha M"
print(friendsList)

friendsList.append("Zainab")
print(friendsList)

newList = friendsList[0:3]
print(newList)

finalFriends = friendsList
print(finalFriends)

position = finalFriends[0:4]
position2 = finalFriends[4:]
#paulPositon = finalFriends /

finalFriends.sort()
print(finalFriends)
finalFriends.sort(reverse = True)
print(finalFriends)
#print(position)


