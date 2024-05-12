artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

unique_artists_1 = set(artist_names)
print("Playlist 1:")
i=1
for artist1 in unique_artists_1:
    print(f"{i}. {artist1}")
    i+=1

j=1
k=1
print("\nPlaylist 2:")
unique_artists_2 = set(artist_names)
for artist2 in unique_artists_2:
    print(f"{j}. {artist2}")
    j+=1

list_1 = list(unique_artists_1)
list_2 = list(unique_artists_2)

a=0
for item in list_1:
    if list_1[a] == list_2[a]:
        a+=1

if a == 4:
    print("Duplicate playlist found.")