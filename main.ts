input.onButtonPressed(Button.A, function () {
    while (true) {
        basic.showString("HI")
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.No)
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
})
basic.showIcon(IconNames.Square)
