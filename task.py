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
