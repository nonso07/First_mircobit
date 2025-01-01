def on_button_pressed_a():
    basic.show_string("HI")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_icon(IconNames.SQUARE)