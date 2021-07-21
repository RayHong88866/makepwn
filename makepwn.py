import os
template ='''
from pwn import *
from Crypto.Util.number import long_to_bytes
import argparse

_Host = ''
_Port = 0;
_File =''
def exp(mode):
    if mode == 0:        
        p = process(_File)
    else:
        p = remote(_Host,_Port)


    p.interactive()    
    
def arg_pase():
    parse = argparse.ArgumentParser()
    parse.add_argument('-d',help='Debug mode',action='count')
    parse.add_argument('-l',help='Local file attach',action='count')
    parse.add_argument('-r',help='Remote \{ip\:port\}')
    parse.add_argument('-f',help='filename')
    return parse.parse_args()


if __name__ ==  '__main__':
    args = arg_pase()
    if args.f != None:        
        if args.d == 1:
            context.log_level = 1
        if args.l == 1:
            _Host = 'localhost'
            _File = str(args.f)
            print(str(args.f))
            exp(0)
        elif len(str(args.r)) > 10 :
            _Host = str(args.r).split(':')[0]
            _Port = str(args.r).split(':')[1]
            _File = str(args.f)            
            exp(1)
        else:
            print('python3 solve.py -l -d // attach local file and debug mode')
            print('python3 solve.py -r 10.10.10.10:1234 // nc remote mode')
    else:
        print('python3 solve.py -f filename')
'''

if os.path.isfile('solve.py') == False:
    f = open('solve.py','w')
    f.write(template)
