from gpiozero import LightSensor

ldr = LightSensor(4)    # pin ke 4

while True:
    print(ldr)

    if ldr < 0.5:
        print("Redup")
    else:
        print("Terang")