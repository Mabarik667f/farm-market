CREATE OR REPLACE PROCEDURE create_user(
    username CHARACTER VARYING(150),
    email CHARACTER VARYING(254),
    password CHARACTER VARYING(128),
    is_active BOOLEAN,
    is_staff BOOLEAN,
    is_superuser BOOLEAN,
    date_joined TIMESTAMP WITH TIME ZONE ,
    first_name CHARACTER VARYING(150),
    last_name CHARACTER VARYING(150),
    img CHARACTER VARYING(100)
)

LANGUAGE SQL
AS $$
INSERT INTO user_customuser (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, img)
VALUES(password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, img)
$$;

CREATE OR REPLACE PROCEDURE create_profile(
    user_id BIGINT,
    address CHARACTER VARYING(255) DEFAULT NULL,
    phone CHARACTER VARYING DEFAULT NULL
)
LANGUAGE SQL
AS $$
INSERT INTO user_profile (user_id, address, phone) VALUES (user_id, address, phone)
$$;

CREATE OR REPLACE PROCEDURE create_role(name CHARACTER VARYING)
LANGUAGE SQL
AS $$
INSERT INTO user_role (name) VALUES (name)
$$;

CREATE OR REPLACE PROCEDURE add_role_for_user(user_id BIGINT, role_id BIGINT)
LANGUAGE SQL
AS $$
INSERT INTO user_roleforuser (user_id, role_id) VALUES (user_id, role_id)
$$;

CREATE OR REPLACE PROCEDURE create_category(cat_name CHARACTER VARYING)
LANGUAGE SQL
AS $$
INSERT INTO category_category (name) VALUES (cat_name)
$$;

CREATE OR REPLACE PROCEDURE create_category_has_product(category_id BIGINT, product_id BIGINT)
LANGUAGE SQL
AS $$
INSERT INTO category_categoryhasproduct (category_id, product_id) VALUES (category_id, product_id)
$$;

CREATE OR REPLACE PROCEDURE create_product(
    name CHARACTER VARYING(255),
    price INTEGER,
    count INTEGER,
    mass NUMERIC,
    shelf_life DATE,
    about JSONB,
    img CHARACTER VARYING,
    seller_id BIGINT
)
LANGUAGE SQL
AS $$
INSERT INTO product_product (name, price, count, about, img, seller_id, mass, shelf_life)
VALUES (name, price, count, about, img, seller_id, mass, shelf_life)
$$;

CREATE OR REPLACE PROCEDURE create_cart_item(
    product_id BIGINT,
    user_id BIGINT,
    count INTEGER,
    delivery_date TIMESTAMP WITH TIME ZONE
)
LANGUAGE SQL
AS $$
INSERT INTO cart_cartitem (product_id, user_id, count, delivery_date)
VALUES (product_id, user_id, count, delivery_date)
$$;

CREATE OR REPLACE PROCEDURE create_order(
    user_id BIGINT,
    address CHARACTER VARYING(255),
    phone CHARACTER VARYING,
    created TIMESTAMP WITH TIME ZONE
)
LANGUAGE SQL
AS $$
INSERT INTO order_order (address, phone, user_id, created)
VALUES (address, phone, user_id, created)
$$;

CREATE OR REPLACE PROCEDURE create_order_item(
    order_id BIGINT,
    product_id BIGINT,
    count INTEGER,
    delivery_date TIMESTAMP WITH TIME ZONE
)
LANGUAGE SQL
AS $$
INSERT INTO order_orderitem (order_id, product_id, count, delivery_date)
VALUES (order_id, product_id, count, delivery_date)
$$;

CREATE OR REPLACE PROCEDURE create_history(profile_id BIGINT, order_id BIGINT)
LANGUAGE SQL
AS $$
INSERT INTO order_history (profile_id, order_id) VALUES (profile_id, order_id)
$$;
