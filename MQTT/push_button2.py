from gpiozero import Button

button = Button(22)
print("Waiting for button")
button.wait_for_press()
print("Button was pressed")
