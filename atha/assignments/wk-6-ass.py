# 1. READ UP ON DICTIONARIES AND LISTS

# DICTS - https://realpython.com/python-dicts/
# LISTS - https://realpython.com/python-lists-tuples/

# 2. WRITE A PYHON PROGRAM TO TAKE IN A SENTENCE, AND THEN COUNT THE NUMBER OF OCCURENCES FOR ALL VOWELS IN THE SENTENCE.

# 3. USING EXHAUSTIVE ENUMERATION SOLVE THE IMAGE BELOW CALLED EXHAUSTIVE ENUMERATION


num_range = range(100, 340)

for value in num_range:
    
    if str(value)[-1]*3 == str(value*3):

        print(value)
