from machine import Pin, Timer 
from ir_rx.acquire import test
test()
# from ir_rx.print_error import print_error  # Optional print of error codes


# def blink(timer):
#     onOff.toggle()
#     #onOff.on()
#     #onOff.off()

# def readIr(timer):
#     print("hello")
#     print(ir.value())

# def ir_command(data, addr, ctrl):
#     if data < 0:  # NEC protocol sends repeat codes.
#         print('Repeat code.')
#         power2.toggle()
#     else:
#         power2.toggle()
#         print('Data {:02x} Addr {:04x}'.format(data, addr))

# ir = IR_GET(Pin(15, Pin.IN), ir_command)
# onOff  = Pin(16, Pin.OUT)
# power2 = Pin(17, Pin.OUT)
# power3 = Pin(18, Pin.OUT)
# power4 = Pin(18, Pin.OUT)
# light  = Pin(18, Pin.OUT)
# print("IR GET")

# timer = Timer()
# #timer.init(freq=1, mode=Timer.PERIODIC, callback=blink)
# ir.error_function(print_error)  # Show debug information
