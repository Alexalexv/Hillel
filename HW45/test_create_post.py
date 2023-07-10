def test_create_post(client):
    client.create_user()
    test_title = 'Its my title'
    test_body = 'Its my body'
    response_create = client.create_post(test_title, test_body)
    assert response_create.status_code == 201

    response_get = client.get_post_by_id(response_create.id)
    assert response_get.title == test_title
    assert response_get.body == test_body
