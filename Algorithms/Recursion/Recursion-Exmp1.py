##make a pile of boxes to look through
#Grab a box and look through
#if you find a box, add it to the pile to look through
#If you find a key, you're done
#Repeat

def find_key(main_box):
    pile = main_box.make_pile_look_through()
    
    while pile is not empty:
        box = pile.grab_a_box
        for item in box:
            if item.is_a_box:
                pile.append(item)
            else:
                print('Found Key')        