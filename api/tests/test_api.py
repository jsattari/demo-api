def test_get_recipes(client):
    """Verify endpoint for all recipes operates correctly"""
    output = client.get("/recipes")
    assert output.status_code == 200

def test_get_breakfast(client):
    """Verify endpoint for all breakfast operates correctly"""
    output = client.get("/breakfast")
    assert output.status_code == 200

def test_get_lunch(client):
    """Verify endpoint for all lunch operates correctly"""
    output = client.get("/lunch")
    assert output.status_code == 200

def test_get_dinner(client):
    """Verify endpoint for all dinner operates correctly"""
    output = client.get("/dinner")
    assert output.status_code == 200