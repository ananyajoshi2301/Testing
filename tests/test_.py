from app import app
def test_index():
    # res = client.get('/')
    response = app.test_client().get('/')
    assert response.status_code == 400
    assert response.data == b'Hello World'
    # expected = "HEllo World"
    # assert expected == res.get_data(as_text=True)