#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

def search_recipes_by_ingredients(ingredients):
    api_key = '479f2282be6b465898717127d6c9de36'
    base_url = 'https://api.spoonacular.com/recipes/findByIngredients'
    
    params = {
        'apiKey':  api_key,
        'ingredients': ','.join(ingredients),
        'number': 5  # number of recipes to retrieve
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        recipes = response.json()
        
        if recipes:
            for recipe in recipes:
                print(f"Title: {recipe['title']}")
                print(f"Missing Ingredients: {recipe['missedIngredientCount']}")
                print(f"Used Ingredients: {recipe['usedIngredientCount']}")
                print("---------------------")
        else:
            print("No recipes found.")
    else:
        print("Failed to fetch recipes.")

# Example usage
ingredients =list(map(str,input().split()))
search_recipes_by_ingredients(ingredients)


# In[ ]:




