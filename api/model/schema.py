import datetime as dt

from marshmallow import Schema, fields


class Recipe():
  def __init__(self, name, ingredients, instructions, type):
    self.name = name
    self.ingredients = ingredients
    self.instructions = instructions
    self.created_at = dt.datetime.now()
    self.type = type

  def __repr__(self):
    return f"<Recipe(name={self.name})>"


class RecipeSchema(Schema):
  name = fields.Str()
  ingredients = fields.List(fields.String())
  created_at = fields.Date()
  instructions = fields.List(fields.String())
  type = fields.Str()