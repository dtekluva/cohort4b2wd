# 3. THREE FRIENDS WHO LOVE EACH OTHER A LOT ALWAYS HAVE SWEETS FROM THEIR PARENTS. WHATS THEY DO IS ADD EVERYBODY'S SWEETS AND THEN SHARE THEM EQUALLY AMONGST THEM SELVES AND THEN CRUSH THE REMAINDER.
#  PLEASE CREATE A SMALL PROGRAM TO AID THE FRIENDS CALCULATE EACH PERSONS SHARE.

# IF INPUTS ARE AS SUCH 

# >>>FRIEND1_SWEETS = 5
# >>>FRIEND2_SWEETS = 6
# >>>FRIEND5_SWEETS = 6

# YOUR RESULT CAN BE AS SUCH 

# >>> HELLO GUYS, EACH OF YOU SHOULD GET 5SWEETS AND 2 SHOULD BE DISCARDED
friend1_sweet = int(input('FRIEND1_SWEETS: '))
friend2_sweet = int(input('FRIEND2_SWEETS: '))
friend3_sweet = int(input('FRIEND3_SWEETS: '))
sum_up = friend1_sweet + friend2_sweet + friend3_sweet
division = sum_up // 3
to_be_discard = sum_up % 3

print(f'HELLO GUYS, EACH OF YOU SHOULD GET {division} SWEETS AND {to_be_discard} SHOULD BE DISCARDED')