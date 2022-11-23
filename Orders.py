import Data_tier


class Orders():
    def __init__(self) -> None:
        self.item_type = "orders"    
        self.content = Data_tier.get_data_and_return_as_list_of_dict(self) 
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]
