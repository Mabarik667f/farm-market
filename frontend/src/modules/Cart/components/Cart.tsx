import { useEffect, useState } from "react";
import CartItem from "./CartItem";
import getCart from "../api/getCart";
import ICartItem from "../interfaces/ICartItem";
import dateFormat from "../helpers/dateFormat";
import CreateOrder from "./CreateOrder";
import delFromCart from "../api/delFromCart";

const Cart = (): JSX.Element => {
  const [cart, setCart] = useState<ICartItem[]>([]);
  const [selected, setSelected] = useState<number[]>([]);
  useEffect(() => {
    const getItems = async () => {
      const newCart = await getCart();
      if (newCart) {
        setCart(newCart);
      }
    };
    getItems();
  }, []);

  const handleSelect = (id: number, isSelected: boolean) => {
    setSelected((prevSelected) =>
      isSelected
        ? [...prevSelected, id]
        : prevSelected.filter((item) => item !== id),
    );
  };

  const handleRemove = async (id: number) => {
    setCart((prevCart) => prevCart.filter((item) => item.id !== id));
    setSelected((prevSelected) => prevSelected.filter((item) => item !== id));
    await delFromCart(id);
  };

  return (
    <div className="flex justify-evenly items-center">
      <div className="flex flex-col justify-center items-center">
        {cart.map(({ product, id, count, delivery_date }) => (
          <div
            className="border-2 border-teal-400 rounded-lg w-100 p-2"
            key={id}
          >
            <CartItem
              product={product}
              count={count}
              isSelected={selected.includes(id)}
              onSelect={(isSelected) => handleSelect(id, isSelected)}
              delivery_date={dateFormat(delivery_date)}
              onRemove={() => handleRemove(id)}
            />
          </div>
        ))}
      </div>
      <CreateOrder selected={selected} />
    </div>
  );
};

export default Cart;
