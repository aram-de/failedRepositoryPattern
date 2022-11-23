import Data_tier

class Products:
    print("Tried to create a product, have not collected data yet")

    def __init__(self) -> None:
        self.item_type = "products"    
        self.content = Data_tier.get_data_and_return_as_list_of_dict(self) 
        self.field_names = ['name', 'price' ]
        print("Tried to created a product")
