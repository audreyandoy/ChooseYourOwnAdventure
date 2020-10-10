import time

print("Welcome to Halloween Horrors")
print()

intro = "It was a foggy cold morning, you walked outside of your door. You can't see anything strangely enough. You head to your car and manage to find the door. After safely getting into your seat.. you hear a voice behind you..."

list = []

for i in intro:
    list.append(i)

for i in list:
 


def start():
    print("It was a foggy cold morning, you walked outside of your door. You can't see anything strangely enough. You head to your car and manage to find the door. After safely getting into your seat.. you hear a voice behind you...")
    time.sleep(5)
    print("Who's there!?")
    for i in range(3):
        print("...")
        time.sleep(1)
    print("You turn around to look at your backseat...")

    scene1 = input("what do you see? \nA) Energizer bunny \nB) A zombie \nC) Your best friend \n")

start()
