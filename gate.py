class Gate():
    def __init__(self, buttons_to_check, starting_state = "CLOSED"):
        self.current_state = starting_state #you can use an enum for states instead of String and is better code practice in Unity
        self.buttons_to_check = buttons_to_check

    def get_state(self):
        return self.current_state

    def open_gate(self):
        self.current_state = "OPENED"
        #lock all buttons
        for button in self.buttons_to_check:
            button.current_state = "LOCKED"

        return

    def check_solution(self):
        f_solved = True  # Set a flag variable to Solved
        for button in self.buttons_to_check:  # for each button
            if button.current_state == "OFF":  # See if any are off
                f_solved = False  # If one is off, not solved

        if f_solved:
            self.open_gate()


    #player_hit isn't needed but I abstracted it in-case later on you want to change "when" you check the solution
    def player_hit(self):
        self.check_solution()
        return

