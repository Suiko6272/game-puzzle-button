class Button():
    def __init__(self, starting_state = "OFF"):
        self.current_state = starting_state #you can use an enum for states instead of String and is better code practice in Unity
        self.buttons_to_effect = []

    def get_state(self):
        return self.current_state

    def add_button_to_effect(self, new_button):
        self.buttons_to_effect.append(new_button)
        return

    def flip_state(self):
        if self.current_state == "LOCKED":
            return
        if self.current_state == "ON":
            self.current_state = "OFF"
        else:
            self.current_state = "ON"

    def effect_other_buttons(self):
        for button in self.buttons_to_effect:       #This is a ForEach in C#
            button.flip_state()
        return

    def player_hit(self):
        self.flip_state()
        self.effect_other_buttons()
        return

