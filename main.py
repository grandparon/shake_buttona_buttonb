MadA = False
MadB = False
MadC = False
basic.show_string("Buttons Please")

def on_forever():
    global MadC, MadB, MadA
    MadC = input.button_is_pressed(Button.A) and input.button_is_pressed(Button.B)
    MadB = input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B)
    MadA = input.is_gesture(Gesture.SHAKE)
    if MadC:
        basic.show_leds("""
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            """)
        basic.pause(200)
    elif MadB:
        basic.show_icon(IconNames.HEART)
        basic.pause(200)
    elif MadA:
        basic.show_string("That Hurts!")
        basic.pause(200)
    else:
        basic.show_leds("""
            # # . # #
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            """)
basic.forever(on_forever)
