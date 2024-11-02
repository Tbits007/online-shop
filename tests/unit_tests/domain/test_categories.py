from app.domain.categories import Categories


def test_categories_model():
    """Тестирует инициализацию модели Categories."""
    
    # Генерируем новый UUID для категории
    category = Categories(
        name="Test Category",
        description="This is a test category."
    )
    
    # Проверяем, что категория была инициализирована с правильными значениями
    assert category.name == "Test Category"
    assert category.description == "This is a test category."
