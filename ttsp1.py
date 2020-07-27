import commands

def espeak(string):
    output = 'espeak "%s"' % string
    a = commands.getoutput(output)



while 1:
	tts=raw_input("what to speak")
	espeak(tts) 
