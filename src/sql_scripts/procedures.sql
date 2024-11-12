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
    img CHARACTER VARYING(100))

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
