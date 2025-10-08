from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_get_all_courses():
    response=client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(),list)


def test_add_courses():
    new_course={ "id": 2, "title": "Data Science", "duration": 1, "fee": 500, "is_active": True }
    response=client.post("/courses",json=new_course)
    assert response.status_code==201
    assert response.json()["title"]=="Data Science"


@pytest.mark.parametrize("course", [
    {"id": 1, "title": "Python Advanced", "duration": 35, "fee": 3500, "is_active": True},
    {"id": 2, "title": "ML Basics", "duration": 25, "fee": 2500, "is_active": True}
])
def test_duplicate_course(course):
    response = client.post("/courses", json=course)
    assert response.status_code == 400
    assert response.json()["detail"] == "Course ID already exists"


def test_invalid_course():
    new_course={ "id": 3, "title": "AI", "duration": 0, "fee": -500, "is_active": True }
    response=client.post("/courses",json=new_course)
    assert response.status_code==422
    assert "greater than" in response.text


def test_get_courses():
    response = client.get("/courses")
    data = response.json()
    assert isinstance(data, list)
    for i in data:
        assert "id" in i
        assert "title" in i
        assert "duration" in i
        assert "fee" in i
        assert "is_active" in i


