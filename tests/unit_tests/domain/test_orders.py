import uuid
from app.domain.orders import Orders, Status


def test_orders_model():
    """Тестирует инициализацию модели Orders."""
    
    # Генерируем новый UUID для заказа и пользователя
    user_id = uuid.uuid4()
    product_id = uuid.uuid4()
    
    # Создаем новый экземпляр Orders
    order = Orders(
        user_id=user_id,
        status=Status.pending, 
        product_id=product_id,
        total_price=29.99,
    )
    
    # Проверяем, что заказ был инициализирован с правильными значениями
    assert order.user_id == user_id
    assert order.status == Status.pending
    assert order.product_id == product_id
    assert order.total_price == 29.99
