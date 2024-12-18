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

CREATE OR REPLACE FUNCTION call_create_history()
RETURNS TRIGGER AS $$
DECLARE profile_id BIGINT;
BEGIN
    WITH cte1 AS (SELECT o.user_id FROM order_order o ORDER BY created DESC LIMIT 1)
    SELECT p.user_id INTO profile_id FROM user_profile p INNER JOIN cte1 ON p.user_id = cte1.user_id;
    CALL create_history(profile_id, NEW.id);
    RETURN NEW;
END
$$ LANGUAGE plpgsql;
