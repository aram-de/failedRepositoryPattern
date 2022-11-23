# The presentation tier is the user 
# interface and communication layer
# of the application, where the end
# user interacts with the application. 
# Its main purpose is to display information
# to and collect information from the user. 
import Orders
import Products
import Couriers
import sys

def show_menu(object):
    print("Show menu running")
    menu_string = f"""Choose an option:
        0 to go to main menu
        1 for seeing the list of {object.item_type}
        2 to add a new {object.item_type}
        3 to update/replace {object.item_type}
        4 to delete {object.item_type}"""
    print(menu_string)
    try:
        u_input = int(input())
        valid_choices = [num for num in range(4)]
        while u_input not in valid_choices:
            print("Not a valid option. Try again.")
            print(menu_string)
            u_input = int(input())
            print("")
        if u_input == 0:
            menu()
        elif u_input == 1:
            object.show_items()
            print("")
            object.show_menu()
        elif u_input == 2:
            object.add_item_to_file()
            print("")
            object.show_menu()
        elif u_input == 3:
            object.update_item()
            print("")
            object.show_menu()
        elif (u_input == 4 and object.item_type != "orders") or (u_input == 5 and object.item_type == "orders"):
            object.delete_item()
            print("")
            object.show_menu()
        elif u_input == 4 and object.item_type == "orders":
            object.update_status()
            print("")
            object.show_menu()
    except SystemExit:
        print("Thank you for using our CLI")
        return("Exited on purpose")
    except:
        print(f"Invalid input for the specific object menu")
        return "Invalid input"


def menu():
    main_menu_string = """Choose an option:
0 to exit
1 for seeing the products menu
2 for seeing the courier menu
3 for seeing the order menu"""
    print(main_menu_string)
    try:
        u_input = int(input())
        valid_choices = [num for num in range(4)]
        while u_input not in valid_choices:
            print("Not a valid option. Try again.")
            print(main_menu_string)
            u_input = int(input())
            print("")
        if u_input == 0:
            sys.exit(0)
        elif u_input == 1:
            print("Opened product menu")
            object = Products.Products()
            print("Created a product object")
            show_menu(object)
        elif u_input == 2:
            print("Opened courier menu")
            object = Couriers.Couriers()
            show_menu(object)
        elif u_input == 3:
            print("Opened order menu")
            object = Orders.Orders()
            show_menu(object)
    except SystemExit:
        print("Thank you for using our CLI")
        return("Exited on purpose")
    except:
        print("Invalid input for the main menu")
        return "Invalid input"

menu()