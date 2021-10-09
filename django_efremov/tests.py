

def test_index_page(client):
    url = ''
    response = client.get(url)
    assert response.status_code == 200


def test_admin_page(client):
    url = 'admin/'
    response = client.get(url)
    assert response.status_code == 200


def test_contact_us_page(client):
    url = 'contact_us'
    response = client.get(url)
    assert response.status_code == 200
