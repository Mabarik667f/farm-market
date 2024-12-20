SET
    client_encoding TO 'UTF8';

CALL create_role ('S');

CALL create_role ('A');

CALL create_role ('D');

--Wholesaller
CALL create_role ('W');

--Processor
CALL create_role ('P');

--Logistician
CALL create_role ('L');

--Agent
CALL create_role ('Ag');

CALL create_user (
    'admin',
    'admin@example.com',
    'password1',
    TRUE,
    TRUE,
    TRUE,
    NOW (),
    'Админ',
    'Пользователь',
    'default.jpg'
);

CALL create_user (
    'farmer1',
    'john.doe@example.com',
    'password2',
    TRUE,
    FALSE,
    FALSE,
    NOW (),
    'Джон',
    'Доу',
    'default.jpg'
);

CALL create_user (
    'farmer2',
    'jane.smith@example.com',
    'password3',
    TRUE,
    FALSE,
    FALSE,
    NOW (),
    'Джейн',
    'Смит',
    'default.jpg'
);

CALL create_user (
    'farmer3',
    'alice.johnson@example.com',
    'password4',
    TRUE,
    FALSE,
    FALSE,
    NOW (),
    'Алиса',
    'Джонсон',
    'default.jpg'
);

CALL create_user (
    'buyer1',
    'bob.brown@example.com',
    'password5',
    TRUE,
    FALSE,
    FALSE,
    NOW (),
    'Боб',
    'Браун',
    'default.jpg'
);

CALL create_user (
    'buyer2',
    'charlie.davis@example.com',
    'password6',
    TRUE,
    FALSE,
    FALSE,
    NOW (),
    'Чарли',
    'Дэвис',
    'default.jpg'
);

CALL create_user (
    'buyer3',
    'diana.wilson@example.com',
    'password7',
    TRUE,
    FALSE,
    FALSE,
    NOW (),
    'Диана',
    'Уилсон',
    'default.jpg'
);

-- Добавление ролей
CALL add_role_for_user (1, 1);

CALL add_role_for_user (1, 2);

CALL add_role_for_user (2, 1);

CALL add_role_for_user (3, 1);

CALL add_role_for_user (4, 1);

CALL create_category ('Овощи');

CALL create_category ('Фрукты');

CALL create_category ('Молочные продукты');

CALL create_category ('Мясо и птица');

CALL create_category ('Зелень и специи');

CALL create_category ('Мёд и джемы');

CALL create_category ('Орехи и сухофрукты');

CALL create_product (
    'Морковь',
    50,
    100,
    700.0,
    '2025-01-01',
    '{"описание": "Сочная, свежая морковь с фермы"}',
    'carrot.jpg',
    2
);

CALL create_product (
    'Яблоки',
    100,
    200,
    700.0,
    '2025-01-01',
    '{"описание": "Красные и зелёные яблоки, выращенные без химии"}',
    'apple.jpg',
    2
);

CALL create_product (
    'Коровье молоко',
    60,
    50,
    700.0,
    '2025-01-01',
    '{"описание": "Натуральное молоко с фермы"}',
    'milk.jpg',
    3
);

CALL create_product (
    'Куриное мясо',
    300,
    30,
    700.0,
    '2025-01-01',
    '{"описание": "Свежая фермерская курица"}',
    'chicken.jpg',
    3
);

CALL create_product (
    'Базилик',
    30,
    40,
    700.0,
    '2025-01-01',
    '{"описание": "Ароматный базилик"}',
    'basil.jpg',
    4
);

CALL create_product (
    'Мёд липовый',
    500,
    20,
    700.0,
    '2025-01-01',
    '{"описание": "Натуральный липовый мёд"}',
    'honey.jpg',
    4
);

CALL create_product (
    'Грецкие орехи',
    400,
    15,
    700.0,
    '2025-01-01',
    '{"описание": "Свежие очищенные орехи"}',
    'walnuts.jpg',
    4
);

CALL create_category_has_product (1, 1);

-- Морковь -> Овощи
CALL create_category_has_product (2, 2);

-- Яблоки -> Фрукты
CALL create_category_has_product (3, 3);

-- Коровье молоко -> Молочные продукты
CALL create_category_has_product (4, 4);

-- Куриное мясо -> Мясо и птица
CALL create_category_has_product (5, 5);

-- Базилик -> Зелень и специи
CALL create_category_has_product (6, 6);

-- Мёд липовый -> Мёд и джемы
CALL create_category_has_product (7, 7);

-- Грецкие орехи -> Орехи и сухофрукты
CALL create_cart_item (1, 5, 2, NOW () + INTERVAL '3 days');

-- Морковь для Покупателя 1
CALL create_cart_item (2, 5, 3, NOW () + INTERVAL '4 days');

-- Яблоки для Покупателя 1
CALL create_cart_item (3, 6, 1, NOW () + INTERVAL '5 days');

-- Молоко для Покупателя 2
CALL create_cart_item (4, 6, 2, NOW () + INTERVAL '6 days');

-- Курица для Покупателя 2
CALL create_cart_item (5, 7, 1, NOW () + INTERVAL '7 days');

-- Базилик для Покупателя 3
CALL create_cart_item (6, 7, 1, NOW () + INTERVAL '8 days');

-- Мёд для Покупателя 3
CALL create_cart_item (7, 7, 1, NOW () + INTERVAL '9 days');

-- Орехи для Покупателя 3
CALL create_order (5, '123 Главная улица', '71234567890', NOW ());

CALL create_order (6, '456 Улица Дуба', '71234567891', NOW ());

CALL create_order (7, '789 Улица Сосен', '71234567892', NOW ());

CALL create_order (5, '321 Улица Ясеней', '71234567893', NOW ());

CALL create_order (6, '654 Улица Берёз', '71234567894', NOW ());

CALL create_order (7, '987 Улица Кленов', '71234567895', NOW ());

CALL create_order (5, '999 Улица Солнца', '71234567896', NOW ());

CALL create_order_item (1, 1, 2, NOW () + INTERVAL '3 days');

-- Морковь в заказе 1
CALL create_order_item (1, 2, 3, NOW () + INTERVAL '4 days');

-- Яблоки в заказе 1
CALL create_order_item (2, 3, 1, NOW () + INTERVAL '5 days');

-- Молоко в заказе 2
CALL create_order_item (2, 4, 2, NOW () + INTERVAL '6 days');

-- Курица в заказе 2
CALL create_order_item (3, 5, 1, NOW () + INTERVAL '7 days');

-- Базилик в заказе 3
CALL create_order_item (3, 6, 1, NOW () + INTERVAL '8 days');

-- Мёд в заказе 3
CALL create_order_item (3, 7, 1, NOW () + INTERVAL '9 days');

-- Орехи в заказе 3
