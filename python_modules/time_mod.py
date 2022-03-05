

import time

# local_time = float(input())
# local_time = local_time * 60
# time.sleep(local_time)
 
from pygame import mixer
# import time

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("song.mp3")

# Setting the volume
mixer.music.set_volume(0.5)

# Start playing the song
# mixer.music.play()

# infinite loop
# while True:
	# 
	# print("Press 'p' to pause, 'r' to resume")
	# print("Press 'e' to exit the program")
	# query = input(" ")
	# 
	# if query == 'p':
# 
		# Pausing the music
		# mixer.music.pause()	
	# elif query == 'r':
# 
		# Resuming the music
		# mixer.music.unpause()
	# elif query == 'e':
# 
		# Stop the mixer
		# mixer.music.stop()
		# break
print(3500/250)
print((8*60)/14)
# after 34.285 min remind water 250 ml
# after every 30 min eyes
# after every 45 min physical work

def water():
	for i in range(8):
		time.sleep(8)
		print("It's Water time\nWater Code = ")
		mixer.music.play()
		input()
		if(input=="Drank"):
			mixer.music.stop()
water()




