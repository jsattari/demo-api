from marshmallow import post_load

from .schema import Recipe, RecipeSchema
from .meal_type import MealType


class Dinner(Recipe):
  def __init__(self, name, ingredients, instructions):
    super(Dinner, self).__init__(name, ingredients, instructions, MealType.DINNER)

  def __repr__(self):
    return f"<Meal(name={self.name})>"


class DinnerSchema(RecipeSchema):
  @post_load
  def make_dinner(self, data, **kwargs):
    return Dinner(**data)