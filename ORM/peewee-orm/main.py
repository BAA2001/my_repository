import models
from models import Dish, Ingredient, Restaurant, Rating
from peewee import fn
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    return Dish.select().order_by(Dish.price_in_cents).first()


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    vegetarian_ingredients = Ingredient.select().where(Ingredient.is_vegetarian is True)  # type: ignore
    return Dish.select().where(Dish.ingredients.in_(vegetarian_ingredients))


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    avg_rating = fn.Avg(Rating.rating).alias("avg_rating")
    return (
        Restaurant.select(Restaurant, avg_rating)
        .join(Rating)
        .group_by(Restaurant)
        .order_by(avg_rating.desc())
        .first()
    )


def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    restaurant = Restaurant.select().first()
    new_rating = Rating(restaurant=restaurant, rating=5)
    new_rating.save()


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    vegan_ingredients = Ingredient.select().where(Ingredient.is_vegan == True)
    vegan_dishes = Dish.select().where(Dish.ingredients.in_(vegan_ingredients))
    return Restaurant.select().where(
        Restaurant.opening_time <= "19:00:00",
        Restaurant.closing_time >= "19:00:00",
        Restaurant.dishes.in_(vegan_dishes),
    )


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    cheese_ingredient, created = Ingredient.get_or_create(name="cheese")
    new_dish = Dish(name="Cheese Pizza", ingredients=[cheese_ingredient])
    new_dish.save()
    return new_dish
