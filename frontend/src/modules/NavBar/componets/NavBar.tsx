import LogoutBtn from "@/modules/Profile/components/LogoutBtn";
import { Button } from "@/UI";
import Cookies from "js-cookie";
import { observer } from "mobx-react-lite";
import { NavLink } from "react-router-dom";

const NavBar = observer((): JSX.Element => {
  return (
    <nav className="flex flex-row justify-center">
      <NavLink to="/" className="m-4">
        Главная
      </NavLink>
      <NavLink to="/orders" className="m-4">
        Заказы
      </NavLink>
      <NavLink to="/profile" className="m-4">
        Профиль
      </NavLink>
      <NavLink to="/cart" className="m-4">
        Корзина
      </NavLink>
      {Cookies.get("refresh") ? (
        <LogoutBtn />
      ) : (
        <div className="flex justify-center items-center">
          <NavLink to="/login" className="m-4">
            Войти
          </NavLink>
          <NavLink to="/register" className="m-4">
            Зарегистироваться
          </NavLink>
        </div>
      )}
    </nav>
  );
});

export default NavBar;
