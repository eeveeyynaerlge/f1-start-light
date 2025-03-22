def on_button_pressed_a():
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(randint(500, 5000))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
