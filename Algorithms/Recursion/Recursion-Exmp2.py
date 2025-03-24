#Look through the box
#if you find a box, go to step 1
#If you find a key, you're done

def find_key(box):
    while box is True:
        for item in box:
            if item.is_a_key:
                print('Found Key')
            elif item.is_a_box:
                look_for_key(item)