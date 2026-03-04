def test_create_address(client):
    response = client.post(
        "/api/v1/addresses/",
        json={
            "street": "Anna Salai",
            "city": "Chennai",
            "country": "India",
            "latitude": 13.0827,
            "longitude": 80.2707,
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["street"] == "Anna Salai"
    assert data["city"] == "Chennai"
    assert "id" in data


def test_get_all_addresses(client):
    response = client.get("/api/v1/addresses/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_address(client):

    create = client.post(
        "/api/v1/addresses/",
        json={
            "street": "MG Road",
            "city": "Bangalore",
            "country": "India",
            "latitude": 12.9716,
            "longitude": 77.5946,
        },
    )

    address_id = create.json()["id"]

    response = client.get(f"/api/v1/addresses/{address_id}")

    assert response.status_code == 200
    assert response.json()["id"] == address_id


def test_update_address(client):

    create = client.post(
        "/api/v1/addresses/",
        json={
            "street": "Old Street",
            "city": "Chennai",
            "country": "India",
            "latitude": 13.0827,
            "longitude": 80.2707,
        },
    )

    address_id = create.json()["id"]

    response = client.put(
        f"/api/v1/addresses/{address_id}",
        json={"street": "New Street"},
    )

    assert response.status_code == 200
    assert response.json()["street"] == "New Street"


def test_delete_address(client):

    create = client.post(
        "/api/v1/addresses/",
        json={
            "street": "Delete Street",
            "city": "Delhi",
            "country": "India",
            "latitude": 28.6139,
            "longitude": 77.2090,
        },
    )

    address_id = create.json()["id"]

    response = client.delete(f"/api/v1/addresses/{address_id}")

    assert response.status_code == 200


def test_nearby_addresses(client):

    client.post(
        "/api/v1/addresses/",
        json={
            "street": "Nearby Street",
            "city": "Chennai",
            "country": "India",
            "latitude": 13.0827,
            "longitude": 80.2707,
        },
    )

    response = client.get(
        "/api/v1/addresses/nearby?lat=13.0827&lon=80.2707&distance_km=5"
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
