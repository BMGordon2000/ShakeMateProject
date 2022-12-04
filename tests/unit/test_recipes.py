def test_recipes(client):
    response = client.get("/recipes")
    assert b"<title>ShakeMate | Recipes</title>" in response.data # b next to it because it is a byte type; could be converted but easier to do this way
