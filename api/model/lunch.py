from marshmallow import post_load

from .schema import Recipe, RecipeSchema
from .meal_type import MealType


class Lunch(Recipe):
  def __init__(self, name, ingredients, instructions):
    super(Lunch, self).__init__(name, ingredients, instructions, MealType.LUNCH)

  def __repr__(self):
    return f"<Meal(name={self.name})>"


class LunchSchema(RecipeSchema):
  @post_load
  def make_lunch(self, data, **kwargs):
    return Lunch(**data)