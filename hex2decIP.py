import signal, sys

def handler(sig, frame):
    print ('\nExiting...')
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

print('Insert your hex IP address or Ctl+C to quit')
while True:
    hex_ip = input('> ')
    if len(hex_ip) == 8:
        try:
            fq = int(hex_ip[6:], 16)
            sq = int(hex_ip[4:6], 16)
            tq = int(hex_ip[2:4], 16)
            lq = int(hex_ip[:2], 16)
            print (f'The well-know ip is: {fq}.{sq}.{tq}.{lq}')
        except:
            print ('There is not a correct format')
    else:
        print ('Something went wrong!')
