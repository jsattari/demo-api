import os

# os.system("./bootstrap.sh & ")

tests = """
# get all recipes
curl -i http://127.0.0.1:5000/recipes
# get all breakfast
curl http://localhost:5000/breakfast
# get all lunch
curl http://localhost:5000/lunch
# get all dinner
curl http://localhost:5000/dinner
# add breakfast item
curl -X POST -H "Content-Type: application/json" -d '{"name": "coffee","ingredients": ["water", "coffee beans"], "instructions":["put coffee beans in cup", "fill cup with boiling water"]}' http://localhost:5000/breakfast
"""

for line in tests.strip().split('\n'):
    print('\n{}'.format(line))
    if not line.startswith('#'):
        cmd = line.strip() 
        os.system(cmd)