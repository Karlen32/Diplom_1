from database import Database
from bun import Bun
from ingredient import Ingredient


def test_database_available_buns():
    database = Database()
    buns = database.available_buns()

    assert isinstance(buns, list)
    assert all(isinstance(bun, Bun) for bun in buns)
    assert len(buns) > 0


def test_database_available_ingredients():
    database = Database()
    ingredients = database.available_ingredients()

    assert isinstance(ingredients, list)
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    assert len(ingredients) > 0