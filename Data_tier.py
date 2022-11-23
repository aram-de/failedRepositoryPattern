# The data tier, sometimes called database
# tier, data access tier or back-end, 
# is where the information processed by
# the application is stored and managed.
import csv
from pathlib import Path

def show_items(object) -> str:
    list_of_dict = object.content
    if list_of_dict == []:
        print(f"There are no {object.item_type}s currently in the system")
        return "No data on file or no file exist"
    else:
        for num, line in enumerate(list_of_dict):      
            print(f"{object.item_type[:-1].capitalize()} n.{num+1}")
            for key, value in line.items():
                key_4_string = key.replace("_", " ").title()
                print(f"\t{key_4_string}: {value}")
            print("")
    return "File content displayed"


def write_to_storage(object):
    file_to_open = Path(f"data/{object.type}.csv")
    with open(file_to_open, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= object.field_names)
            writer.writeheader()
            for dictio in object.content:
                writer.writerow(dictio)

def get_data_and_return_as_list_of_dict(object) -> list:
        """ as per name, if fails returns error"""
        try:
            file_to_open = Path(f"data/{object.type}.csv")
            with open(file_to_open, "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                list_of_records = (list(records))
            return list_of_records
        except FileNotFoundError as e:
            #print(rf"{e}.\nFailed to load data requested. Try adding one {self.item_type} first.")
            return e #check with Patrick

def delete_item(object):
    show_items(object)
    list_of_dicts = object.content
    if len(list_of_dicts) == 1:
        print("The are no items to delete") 
        Presentation_tier.show_menu(object) 
    else:
        try:
            print(f"Enter the number for the {object.type[:-1]} you want to delete: ")
            deletee = input()              
            lines = object.content
            del lines[int(deletee+1)] #needs the plus one to be consistent with the file because of headers
            object.content = lines #updates but no permanence yet
            write_to_storage(object)
            print(f"{object.type[:-1]} number {deletee+1} is now deleted.")
            Presentation_tier.show_menu(object)
        except IndexError:
            print("\n\n\n  You entered an invalid number. \n\n\n")
            print("\n\n\n  Back to the menu. \n\n\n")
            Presentation_tier.show_menu(object)

        except TypeError:
            print("\n\n\n  You did not enter a whole number \n\n\n")                
            print("\n\n\n  Back to the menu. \n\n\n")
            Presentation_tier.show_menu(object)