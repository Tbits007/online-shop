import uuid
from app.domain.products import Products


def test_products_model():
    """Тестирует инициализацию модели Products."""

    product = Products(
        name="Test Product",
        description="This is a test product.",
        price=19.99,
        currency="USD",
        stock=100,
        category_id=uuid.uuid4()  # Здесь может быть id существующей категории
    )
    
    # Проверяем, что продукт был инициализирован с правильными значениями
    assert product.name == "Test Product"
    assert product.description == "This is a test product."
    assert product.price == 19.99
    assert product.currency == "USD"
    assert product.stock == 100
    assert product.category_id is not None  # Проверяем, что category_id не None
