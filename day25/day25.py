door_public_key = 10212254
card_public_key = 12577395
modulus = 20201227
subject = 7
value = 1
loop_size = 0
card_loop_size = None
door_loop_size = None
count = 1
while card_loop_size is None or door_loop_size is None:
    value = (value * subject) % modulus
    if value == door_public_key:      
        door_loop_size = count
    elif value == card_public_key:
        card_loop_size = count
    count = count + 1

value = 1
subject = door_public_key
for _ in range(card_loop_size):
    value = (value * subject) % modulus

print(value)