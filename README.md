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
```python
from wrapper import EANData

x = EANData'API_KEY')

x.get_barcode_data('ean_code')
```

### Locu
```python
from wrapper import Locu

x = Locu('API_KEY')

search_restaurant(**kwargs)
get_restaurant_details(venue_id)
get_restuarants_with_menu(query)
```

### Spoonacular
```python
from wrapper import Spoonacular

x = Spoonacular('API_KEY')

get_recipe_by_ingredients(ingredients=None)
get_recipe_by_id(recipe_id=None)
generate_meal_plan(**kwargs)
map_ingredients_to_grocery(data)
get_random_recipe(**kwargs)
search_recipies(**kwargs)
```

### Walmart
```python
from wrapper import Walmart

x = Walmart('API_KEY')

search_item(term)
get_food_products(category_id='976759')
product_recommendation(product_id)
product_history(product_id)
get_item_review(product_id)
get_best_sellers(category_id='976759')
get_rollback_items(category_id='976759')
get_clearance_items(category_id='976759')
store_locator(**kwargs)
# kwargs examples for store_locator
# city :string ('New York')
# zip :string (10001)
# cordinates :string ('lat,lon') ('40.7128,74.0059')
```

### Zomato
```python
from wrapper import Zomato

x = Zomato('API_KEY')

get_categories()
get_city(**kwargs)
get_collections(**kwargs)
get_cuisines(**kwargs)
get_restaurant_types(**kwargs)
search(**kwargs)
get_top_restaurants(location_id, entity_type='city')
get_daily_menu(restaurant_id)
geocode(latlon)
get_restaurant_details(restaurant_id)
get_restaurant_review(restaurant_id)
```
