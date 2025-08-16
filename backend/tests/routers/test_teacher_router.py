from fastapi.testclient import TestClient
from app.models import Teacher


def test_create_student_unauthenticated(client: TestClient) -> None:
    """Creating a student without authentication should fail."""

    response = client.post("/api/teacher/students", json={"name": "Test Student"})

    assert response.status_code == 422


def test_create_student_authenticated(
    client: TestClient, test_teacher: Teacher
) -> None:
    """A teacher can create a student when authenticated."""

    headers = {"X-Teacher-ID": test_teacher.id}
    student_payload = {"name": "Jane Doe", "email": "jane.doe@example.com"}

    response = client.post(
        "/api/teacher/students", headers=headers, json=student_payload
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Jane Doe"
    assert data["id"] is not None


def test_get_students_authenticated(
    client: TestClient, test_teacher: Teacher
) -> None:
    """Authenticated teacher should retrieve their students."""

    headers = {"X-Teacher-ID": test_teacher.id}
    client.post("/api/teacher/students", headers=headers, json={"name": "Student A"})

    response = client.get("/api/teacher/students", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Student A"


def test_create_assignment_authenticated(
    client: TestClient, test_teacher: Teacher
) -> None:
    """Authenticated teacher can create an assignment."""

    headers = {"X-Teacher-ID": test_teacher.id}
    payload = {"title": "My Assignment"}

    response = client.post("/api/teacher/assignments", headers=headers, json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My Assignment"
    assert data["assignment_id"] is not None
    assert data["status"] == "draft"
    assert data["canvas_json"] == []


def test_create_assignment_missing_header(client: TestClient) -> None:
    """Missing authentication header should result in validation error."""

    response = client.post("/api/teacher/assignments", json={"title": "Test"})

    assert response.status_code == 422


def test_create_material_authenticated(
    client: TestClient, test_teacher: Teacher
) -> None:
    """Authenticated teacher can create material."""

    headers = {"X-Teacher-ID": test_teacher.id}
    payload = {
        "title": "Chapter 1",
        "content": "Content for chapter 1"
    }

    response = client.post("/api/teacher/materials", headers=headers, json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Chapter 1"
    assert data["content"] == "Content for chapter 1"
    assert data["id"] is not None


def test_create_material_invalid_payload(
    client: TestClient, test_teacher: Teacher
) -> None:
    """Invalid payload should trigger validation error."""

    headers = {"X-Teacher-ID": test_teacher.id}
    payload = {"title": "Incomplete"}  # Missing 'content'

    response = client.post("/api/teacher/materials", headers=headers, json=payload)

    assert response.status_code == 422


def test_get_materials_authenticated(
    client: TestClient, test_teacher: Teacher
) -> None:
    """Authenticated teacher should retrieve materials."""

    headers = {"X-Teacher-ID": test_teacher.id}
    client.post(
        "/api/teacher/materials",
        headers=headers,
        json={"title": "Note", "content": "Some content here"},
    )

    response = client.get("/api/teacher/materials", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Note"

