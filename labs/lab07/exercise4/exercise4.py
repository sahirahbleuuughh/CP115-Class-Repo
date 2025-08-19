'''
Uses f-strings to display:

    Welcome message with restaurant name
    Customer number
    Complete menu with all items
    Today's special (based on the random number)
'''
import menu_data

print(f"˖˚⊹ ꣑ৎ\tWELCOME TO {menu_data.upperRestaurant}!\t꣑ৎ ⊹˚˖\n")
print(f"YOUR NUMBER IS: {menu_data.customerNum}\n")
print(f"MENU\n- {menu_data.food}\n- {menu_data.drink}\n- {menu_data.dessert}\n")
if menu_data.specialNumDaily == 1:
    todaySpecial = menu_data.food
elif menu_data.specialNumDaily == 2:
    todaySpecial = menu_data.drink
else:
    todaySpecial = menu_data.dessert
print(f"TODAY'S SPECIAL...! {todaySpecial}\n")
print("\t⊹₊ ˚‧︵‿₊୨ ᰔ ୧₊‿︵‧ ˚ ₊⊹")