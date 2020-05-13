# problem link = https://www.hackerrank.com/challenges/py-the-captains-room/problem
# every one came with family except the captain
# so if a room is assigned to a person with only one member then he must be captain
# I m facing the problem of runtime error, it would be great if you can help me
# in optimising the code


K = input()
room_list_input = input()
room_list = list(map(int, room_list_input.split()))
room_set = list(set(room_list))

for i in room_set:
    room_count = room_list.count(i)

    if room_count == 1:
        print(i)

        break
