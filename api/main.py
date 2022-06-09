#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crypt import methods
from distutils.log import debug
from unicodedata import name
from flask import Flask, request, jsonify
import json

from api.model.schema import Recipe, RecipeSchema
from api.model.breakfast import Breakfast, BreakfastSchema
from api.model.lunch import Lunch, LunchSchema
from api.model.dinner import Dinner, DinnerSchema

from api.model.meal_type import MealType


app = Flask(__name__)

with open("api/data.json", "r") as outfile:
  recipes = json.load(outfile)

meals = [
  Breakfast(
    recipes.get("recipes")[0].get("name"),
    recipes.get("recipes")[0].get("ingredients"),
    recipes.get("recipes")[0].get("instructions")),

  Lunch(
    recipes.get("recipes")[2].get("name"),
    recipes.get("recipes")[2].get("ingredients"),
    recipes.get("recipes")[2].get("instructions")),

  Dinner(
    recipes.get("recipes")[1].get("name"),
    recipes.get("recipes")[1].get("ingredients"),
    recipes.get("recipes")[1].get("instructions"))
]

@app.route('/recipes')
def get_recipes():
  schema = RecipeSchema(many=True)
  all_recipes = schema.dump(meals)
  return jsonify(all_recipes)

@app.route('/breakfast')
def get_breakfast():
  schema = BreakfastSchema(many=True)
  breakfast = schema.dump(
    filter(lambda x: x.type == MealType.BREAKFAST, meals)
  )
  return jsonify(breakfast)

@app.route('/lunch')
def get_lunch():
  schema = LunchSchema(many=True)
  lunch = schema.dump(
    filter(lambda x: x.type == MealType.LUNCH, meals)
  )
  return jsonify(lunch)

@app.route('/dinner')
def get_dinner():
  schema = DinnerSchema(many=True)
  dinner = schema.dump(
    filter(lambda x: x.type == MealType.DINNER, meals)
  )
  return jsonify(dinner)

@app.route('/breakfast', methods=['POST'])
def add_breakfast():
  new_recipe = BreakfastSchema().load(request.get_json())
  bfast_names = [i.name for i in meals]
  try:
    if new_recipe.name not in bfast_names:
      meals.append(new_recipe)
      return '', 204
  except:
    return jsonify("Error: Recipe already exists"), 400

@app.route("/breakfast", methods=["PUT"])
def update_breakfast():
  new_recipe = BreakfastSchema().load(request.get_json())
  existing_recipe = [i for i in meals if i.name == new_recipe.name]
  try:
    if new_recipe.name == existing_recipe[0].name:
      existing_recipe[0].name = new_recipe.name
      existing_recipe[0].ingredients = new_recipe.ingredients
      existing_recipe[0].instructions = new_recipe.instructions
    return "", 204
  except:
    return jsonify("Error: Recipe does not exist"), 400
