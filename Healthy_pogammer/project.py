from pygame import mixer
import time

# Starting the mixer
# mixer.init()

# Loading the song
# mixer.music.load("eyes.mp3")
# mixer.music.load("water.mp3")
# mixer.music.load("physical.mp3")
# 
# Setting the volume
# mixer.music.set_volume(0.5)

# Start playing the song
# mixer.music.play()

# infinite loop
# while True:
	
	# print("Press 'p' to pause, 'r' to resume")
	# print("Press 'e' to exit the program")
	# query = input(" ")
	# 
	# if query == 'p':
# 
		# Pausing the music
		# mixer.music.pause()	
	# elif query == 'r':

		# Resuming the music
		# mixer.music.unpause()
	# elif query == 'e':

		# Stop the mixer
		# mixer.music.stop()
		# break
def water():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(0.5)
    for i in range(8):
        time.sleep(30)
        print("Its Water time")
        while True:
            mixer.music.play()
            w_code = input("Water code is : ")
            if(w_code=="Drank"):
                mixer.music.stop()
                break
        # mixer.music.play()
        # w_code=input("Water code is : ")
        # while(w_code != "Drank" )
water()
    
        
        
