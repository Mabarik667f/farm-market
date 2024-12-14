import { AuthContext } from "@/contexts/AuthContext";
import { Button } from "@/UI";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

const LogoutBtn = (): JSX.Element => {
  const { store } = useContext(AuthContext);
  const navigate = useNavigate();
  const logoutEvent = () => {
    store.logout();
    navigate("/login");
  };
  return (
    <Button className="bg-red-600 mt-4" onClick={logoutEvent}>
      Выйти
    </Button>
  );
};

export default LogoutBtn;
