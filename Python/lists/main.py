# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

#CHANGE ORDER IN LIST WITH FUNCTION

from turtle import clear


list = ['The Imperial March', 'Somewhere in My Memory', 'E.T.: The Flying Theme', 'Hymn to the Fallen', 'Harry’s Wondrous World']

def alphabetical_order(list):
    print(sorted(list))

alphabetical_order(list)

#CHECK MEMBERSHIP IN LIST AND RETURNING TRUE/FALSE WITH FUNCTION

films_won = ['fiddler on the roof','jaws', 'star wars']

def won_golden_globe(film_name):
    film_name.lower() # convert input automatically to lowercase
    if film_name in films_won:  
        return True
    else: return False


won_golden_globe('valley of the dolls')

#REMOVING SPECIFIED ELEMENTS FROM A LIST WITH A FUNCTION 

mixed_albums = ['Tears','I Am Alive', 'Dune', 'Toto']

def remove_toto_albums(list):
    toto_albums = ['I Am Alive', 'Toto']
    for name in toto_albums:
        name.lower()
        if name in list:
            list.remove(name)
    print(list)

remove_toto_albums(mixed_albums)