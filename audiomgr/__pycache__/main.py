#imports
from display import print_menu, print_header, clear
from album import Album
from song import Song
import pickle



#globals
catalog = []
album_count = 0

#git add .     git commit -m "dkdkdd"        git push


#functions

def serialize_data():
    try:
        writer = open('songMngr.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved")



def deserialize_data():
    global album_count

    try:
        reader = open('songMngr.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        # get the last used id, and increase by 1
        last = catalog[-1]
        album_count = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " albums")

    except:
        print("** Error, no data file found")




def register_album():
    global album_count
    print_header("Register New Album")

  
    try:

        title = input("Please Provide Title: ")
        genre = input("Please Provide Genre: ")
        artist = input("Please Provide Artist: ")
        release_year = int(input("Please Provide Release Year: "))
        price = float(input("Please Provide Price: $"))
        album_art = input("Please Provide Album Art URL: ")
        related_artist = input("Please Provide Related Artists: ")
        record_label = input("Please Provide Record Label: ")

        #changes id by 1, look at top by catalog []
        album_count += 1

        album = Album(album_count, title, genre, artist, release_year, price, album_art, related_artist, record_label)
        print(album)

        catalog.append(album)
        print("** Album created!")

    except ValueError:
        print("** Error: Invalid Number. Try again")

    except:
        input("*** Unexpected Error. Try again later")

    

def print_albums():
    print_header("Your current albums")

    for album in catalog:
        print(f"{album.id} | {album.title} | {album.release_year}")



def register_song():
    print_header("Register New Song")

   

    #let user choose album
    print_albums()
    album_id = input("Please choose the album Id:")


    found = False
    for album in catalog:
        if(album.id == album.id):
            found = True
            the_album =album

    if(not found):
        print("** Error: Wrong Id. Try again")
        return



    print_header("Register a new song: ")

    title = input("Please Provide a Title: ")
    featured_artist = input("Featured by: ")
    length_of_track = input("Please Provide Length of Song: ")
    written_by = input("Please Provide Writers Name: ")
    
    song = Song(1,title,featured_artist,length_of_track,written_by)

    #push the song to the album list
    the_album.add_song(song)
    
    print("Song Created!")

def display_album_songs():
    print_header("Your album catalog...")
    print_albums()

    album_id = input("Please choose an ID: ")


    for album in catalog:
        if(album.id == album_id):
            Found = True

            #print album songs
            for song in album.songs:
                print(song.title)
        if(not found):
            print("** Error: Invalid album ID")

    input("Press Enter to continue...")


def count_songs():
    print_header("Your total number of songs")

    total = ''
    for album in catalog:
        songs_catalog = len(album.songs)
        total += songs_catalog

    print(f"There are: {total} songs in the system")



#instructions

deserialize_data()
input("Press Enter to continue...")

opc = ''
while(opc != 'q'):  
    clear()
    print_menu()
    opc = input("Please select an option: ")

        
    if(opc == '1'):
        register_album()
        serialize_data()

    elif(opc == '2'):
        register_song()
        serialize_data()

    elif (opc == '3'):
        display_album_songs()
        serialize_data()

    elif (opc == '4'):
        print_albums()
        serialize_data()

    elif (opc == '5'):
        count_songs()
        serialize_data()
    


        input("Press Enter to continue...")


def print_albums():
    print_header("Your current albums")
    for album in catalog:
        print(album.title)

input("Press enter to continue...")