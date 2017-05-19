from button import Button
from gate import Gate

#Intilize all buttons
a = Button()
b = Button("ON")
c = Button()
d = Button()
solution_list = [a,b,c,d]
final_gate = Gate(solution_list, "CLOSED")

def pretty_print_buttons():
    global a
    global b
    global c
    global d
    global final_gate
    print("Button A: ", a.get_state())
    print("Button B: ", b.get_state())
    print("Button C: ", c.get_state())
    print("Button D: ", d.get_state())
    print("Gate: ", final_gate.get_state())



#Assign which buttons any given button should effect

a.add_button_to_effect(b)
a.add_button_to_effect(c)
a.add_button_to_effect(d)

b.add_button_to_effect(c)

c.add_button_to_effect(d)

# so all will flip themselves
# a will flip all 3. b will flip c, c will flip d, d won't flip any other buttons but itself


print("=== Starting State ===")
pretty_print_buttons()


print("=== Player hits A ===")
a.player_hit()
pretty_print_buttons()

print("=== Player hits Final Button / Gate ===")
print("Since B is off it won't work and nothing changes")
final_gate.player_hit()
pretty_print_buttons()

print("=== Player hits B ===")
b.player_hit()
pretty_print_buttons()

print("=== Player hits C ===")
c.player_hit()
pretty_print_buttons()

print("=== Player hits D ===")
d.player_hit()
pretty_print_buttons()

print("=== Player hits Final Button / Gate ===")
final_gate.player_hit()
pretty_print_buttons()