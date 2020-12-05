let MadA = false
let MadB = false
let MadC = false
basic.showString("Buttons Please")
basic.forever(function () {
    MadC = input.buttonIsPressed(Button.A) && input.buttonIsPressed(Button.B)
    MadB = input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)
    MadA = input.isGesture(Gesture.Shake)
    if (MadC) {
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.pause(200)
    } else if (MadB) {
        basic.showIcon(IconNames.Heart)
        basic.pause(200)
    } else if (MadA) {
        basic.showString("That Hurts!")
        basic.pause(200)
    } else {
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            `)
    }
})
