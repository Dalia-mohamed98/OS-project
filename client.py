import zmq
import sys
import time


port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
print ("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

#  Do 10 requests, waiting each time for a response
#for request in range (1,10):
    
print ("Waiting request...")

read = input()
while(read.find("Upload") == -1):
    print ("Choose 'Upload' or 'show'")
    read = input()
    
socket.send_string(read)
print ("Sending request...")
#time.sleep (1) 

#  Get the reply.
message = socket.recv_string()

print ("Received reply ", message)
