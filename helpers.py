def alphabet_position(letter):
    # Convert alpha char into an uppercase alpha char
    upper_letter = letter.upper()
    # Take the Ascii table position of that number and subtract the ASCII position of 'A' to get alpha position 
    return ord(upper_letter) - 65

def rotate_character(char, rot):
    # Make sure char is alpha:
    if char.isalpha():
        # import pdb;pdb.set_trace()
        
        # Set up variables:  Define the starting point for the char in the alphabet, where the char is in the alphabet, and how much to shift:
        ascii_pos = ord(char)
        position = alphabet_position(char)
        shift = rot % 26
        
        # Account for shift needing to roll back to beginning of alphabet:
        if shift + position > 25:
            shift = (rot % 26) - 26
        
        #Return the char at the starting position plus appropriate shift:
        return chr(ascii_pos + shift)
    
    # If char is not alpha, return as is
    else:
        return char