import Data_tier


class Couriers():
    def __init__(self) -> None:
        self.item_type = "couriers"    
        self.content = Data_tier.get_data_and_return_as_list_of_dict(self) 
        self.field_names = ['name', 'phone' ]
