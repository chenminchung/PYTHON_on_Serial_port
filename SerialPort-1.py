import serial
import os
import time
 
port = "COM17"
baud = 19200

def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    
    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #   
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()        

    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()
 
ser = serial.Serial(port, baud, timeout=1)
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = None

    # open the serial port
if ser.isOpen():
     print(ser.name + ' is open...')
 
while True:

        out = ser.read(22)

        print (out);
        print(ByteToHex(str(out)));

        print (type(out),end=''); print("length=",len(out))

        if b'\xf4' in out : print("end of command")
        z=list(out) # generates a list of codes from the characters of bytes
        chk=0;
        for x in z:

            chk=chk+int(x);

        print("chk=" +str(chk));
        print("first byte="+str(z[0]))
        print("last byte="+str(z[-1]))

        fc = open('ST003','ab') 
        fc.write(out)
        fc.write(b'\x0d') 
        fc.close
        
        print(time.asctime(time.localtime(time.time())))
        
        
        
 
