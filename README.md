# Little Endian Hexadecumal IP to Decimal IP
This script is made for myself to never forget how to do this stuff. Little endian is a format of data representation in memory that storage the information by the less significative byte to the most significative byte.

## How it works
When you type the command ```cat /proc/net/route``` the ip address are show in little endian hexadecimal format, like this:
IMAGEN
So we can observe the ip in that format is ```02 02 00 0A``` so this means ```2 2 0 10``` in decimal, then the decimal ip will be ```10.0.2.2```.

In the study case the ip will result easy to transform but if the ip is more complex will be hard to transform, so I create this python3 script to simplify the process.
```python3
```

As we can observe on the image bellow the traduction is correct. Thanks!
