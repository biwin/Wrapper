# Wrapper

A wrapper around several APIs.

Response is a request object, which is much extendable for custom error handling.

The Available APIs are:

    EANData
    Locu
    Spoonacular
    Walmart
    Zomato


# API Methods


### EANData

    x = EANData(api_key='API_KEY')
    x.get_barcode_data('ean_code')

### Locu

    x = Locu('api_key')
    search_restaurant(self, **kwargs):
    get_restaurant_details(self, venue_id):
    get_restuarants_with_menu(self, query):

### Spoonacular

    from wrapper import Spoonacular
    x = Spoonacular('api_key')

    get_recipe_by_ingredients(self, ingredients=None):
    get_recipe_by_id(self, recipe_id=None):
    generate_meal_plan(self, **kwargs):
    map_ingredients_to_grocery(self, data):
    get_random_recipe(self, **kwargs):
    search_recipies(self, **kwargs):


### Walmart

    from wrapper import Walmart
    x = Walmart('api_key')

    search_item(self, term)
    get_food_products(self, category_id='976759')
    product_recommendation(self, product_id)
    product_history(self, product_id)
    get_item_review(self, product_id)
    get_best_sellers(self, category_id='976759')
    get_rollback_items(self, category_id='976759')
    get_clearance_items(self, category_id='976759')
    store_locator(self, **kwargs)
    # kwargs examples for store_locator
    # city :string ('New York')
    # zip :string (10001)
    # cordinates :string ('lat,lon') ('40.7128,74.0059')

### Zomato

    from wrapper import Zomato
    x = Zomato('api_key')

    get_categories()
    get_city(self, **kwargs)
    get_collections(self, **kwargs)
    get_cuisines(self, **kwargs)
    get_restaurant_types(self, **kwargs)
    search(self, **kwargs)
    get_top_restaurants(self, location_id, entity_type='city')
    get_daily_menu(self, restaurant_id)
    geocode(self, latlon)
    get_restaurant_details(self, restaurant_id)
    get_restaurant_review(self, restaurant_id)
