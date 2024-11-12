CREATE OR REPLACE FUNCTION call_create_profile()
RETURNS TRIGGER AS $$
BEGIN
    CALL create_profile(NEW.id);
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION call_add_default_role_for_user()
RETURNS TRIGGER AS $$
DECLARE role_id BIGINT;
BEGIN
    SELECT r.id INTO role_id FROM user_role r WHERE r.name = 'D';
    CALL add_role_for_user(NEW.id, role_id);
    RETURN NEW;
END
$$ LANGUAGE plpgsql;
