import pytest
import os
# # # #from io import StringIO
# # # #from app4 import Courier
from nuked import *



##TEST GET FILE

#happy

def test_get_file_returns_list():
    an_item = Item_menu()
    content = an_item.get_csv_and_return_as_list_of_dict()
    expected = list
    actual = type(content)
    assert expected == actual


def test_get_file_returns_list_of_dict():
    an_item = Item_menu()
    a_list = an_item.get_csv_and_return_as_list_of_dict()
    expected = dict
    for item in a_list:
        actual = type(item) 
        assert expected == actual

#unhappy

#NOT SURE THIS IS TESTING WHAT I THINK
def test_get_file_returns_error_when_it_fails():
    an_item = Item_menu() #this fails because we are trying to get an item
    an_item.item_type = "Item type that does not exist so no file for it exists"
    #mock data
    expected = FileNotFoundError#(2, 'No such file or directory')
    #with pytest.raises(FileNotFoundError):
    actual = an_item.get_csv_and_return_as_list_of_dict()
    assert expected == type(actual)


##TEST SHOW ITEM

#happy
# def test_show_items_when_there_are():
#     an_item = Item_menu()
#     #stub data
#     an_item.content = [{'name' : "melon", 'age' : 3},  {'name' : "melon2", 'age' : 23}]
#     expected = "File content displayed"
#     actual = an_item.show_items() 
#     assert expected == actual

# #unhappy
# def test_show_items_when_content_empty():
#     an_item = Item_menu()
#     #stub data
#     an_item.content = []
#     expected = "No data on file or no file exist"
#     actual = an_item.show_items() 
#     assert expected == actual


# #TESTING WRITING

# #HAPPY
# def test_write_to_csv_writes():
#     #set up
#     an_item = Item_menu()
#     os.remove(f"data/{an_item.item_type}.csv") #delete file so that we use mock data
#     #Mock data
#     an_item.content = [{'name' : "melon", 'age' : "3"},  {'name' : "melon2", 'age' : "23"}]
#     #action
#     an_item.write_list_of_dict_to_csv()

#     assert an_item.content == an_item.get_csv_and_return_as_list_of_dict()

#DON'T KNOW HOW TO CREATE UNHAPPY CASE
# def test_write_to_csv_writes_fails():
#     """ test failes because he data passed is not a list of dict"""
#     #set up
#     an_item = Item_menu()
#     os.remove(f"data/{an_item.item_type}.csv") #delete file so that we use mock data
#     #Mock data: overwrite object content with empty list  
#     expected =  rf"Failed to load data requested. Try adding one {an_item.item_type[:-1]} first." 
#     an_item.content = None
#     #action
#     an_item.write_list_of_dict_to_csv()

#     assert expected == an_item.get_csv_and_return_as_list_of_dict()


#TESTING ADDING ITEM
#happy

# def test_add_item_succeeds(monkeypatch):
#     an_item_menu = Item_menu()
#     #setup
#     #This fakes manual input
#     answers = iter(["testAdd", "3"])
#     monkeypatch.setattr('builtins.input', lambda _: next(answers, None))
    
#     item_plus_added_content = list(an_item_menu.content).append({'name' : "testAdd", 'age' : "3"})

#     #action
#     assert item_plus_added_content == an_item_menu.add_item()

# #unhappy
# def test_add_item_user_enters_nothing(monkeypatch):
#     an_item_menu = Item_menu()
#     #setup
#     original_item_content = list(an_item_menu.content)
#     #This fakes multiple manual inputs
#     manual_inputs = iter(["", ""])
#     monkeypatch.setattr('builtins.input', lambda _: next(manual_inputs, None))
#     #action
#     assert original_item_content == an_item_menu.add_item()


#Testing get product indexes if it succeeds returns index list





#TESTING selecting ITEM
#happy

# def test_selecting_item_success(monkeypatch):
    











# def test_main_menu_invalid_input(monkeypatch):
#     aMenu = Menu()
#     answers = "Hello"
#     monkeypatch.setattr('builtins.input', lambda : answers)
#     actual = aMenu.menu()
#     expected = "Invalid input"
#     assert actual == expected


# def test_main_menu_choose_one(monkeypatch):
#     aMenu = Menu()
#     answers = 1
#     monkeypatch.setattr('builtins.input', lambda : answers)
#     actual = aMenu.menu()
#     #TEST IF A METHOD HAS BEEN CALLED
#     expected = "Opened product menu"
#     assert actual == expected

# # def test_main_menu_choose_one(monkeypatch, mocker):
# #     answers = 1
# #     monkeypatch.setattr('builtins.input', lambda : answers)
# #     mocked_func = mocker.patch('test.hello')

# #     actual = aMenu.menu()
# #     expected = "Opened product menu"
# #     assert actual == expected


# def test_main_menu_choose_zero(monkeypatch):
#     aMenu = Menu()
#     answers = 0
#     monkeypatch.setattr('builtins.input', lambda : answers)
#     actual = aMenu.menu()
#     expected = "Exited on purpose"
#     assert actual == expected
