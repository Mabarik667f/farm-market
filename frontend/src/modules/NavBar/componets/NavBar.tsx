import { NavLink } from "react-router-dom";

const NavBar = (): JSX.Element => {
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
    </nav>
  );
};

export default NavBar;
