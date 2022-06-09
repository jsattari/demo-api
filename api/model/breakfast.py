from marshmallow import post_load

from .schema import Recipe, RecipeSchema
from .meal_type import MealType


class Breakfast(Recipe):
  def __init__(self, name, ingredients, instructions):
    super(Breakfast, self).__init__(name, ingredients, instructions, MealType.BREAKFAST)

  def __repr__(self):
    return f"<Meal(name={self.name})>"


class BreakfastSchema(RecipeSchema):
  @post_load
  def make_breakfast(self, data, **kwargs):
    return Breakfast(**data)