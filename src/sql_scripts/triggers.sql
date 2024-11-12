CREATE OR REPLACE TRIGGER profile_for_user
AFTER INSERT ON user_customuser
FOR EACH ROW
EXECUTE FUNCTION call_create_profile();

CREATE OR REPLACE TRIGGER default_role_for_user
AFTER INSERT ON user_customuser
FOR EACH ROW
EXECUTE FUNCTION call_add_default_role_for_user();
