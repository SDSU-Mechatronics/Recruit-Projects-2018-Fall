import serial
ser = serial.Serial('/dev/ttyACM0')

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

while True:
	output = raw_input("Enter degrees: ")
	print(output)
	if is_int(output):
		print("In IF")
		ser.write(b''.join(output))
	elif output == "quit":
		break

ser.close()
