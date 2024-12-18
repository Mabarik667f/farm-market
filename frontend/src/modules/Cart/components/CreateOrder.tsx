import { useEffect, useState } from "react";
import INewOrder from "../interfaces/INewOrder";
import { Input, FormInpField, Button } from "@/UI";
import { useNavigate } from "react-router-dom";
import newOrder from "../api/newOrder";

const CreateOrder = ({ selected }: { selected: number[] }): JSX.Element => {
  const [order, setOrder] = useState<INewOrder>({
    address: "",
    phone: "",
    cart_item_ids: selected,
  });

  const navigate = useNavigate();
  useEffect(() => {
    setOrder((prevOrder) => ({
      ...prevOrder,
      cart_item_ids: selected,
    }));
  }, [selected]);
  const createOrder = async (e: React.FormEvent<HTMLFormElement>) => {
    console.log(order);
    e.preventDefault();
    if (order.cart_item_ids.length >= 1) {
      try {
        await newOrder(order);
        navigate("/orders");
      } catch (e) {
        console.log(e);
      }
    } else {
      alert("Выберите товары для заказа!");
    }
  };

  return (
    <div className="flex justify-center items-center border-2 border-teal-400 rounded-lg p-4">
      <form
        method="post"
        className="flex flex-col justify-center items-center mt-2"
        onSubmit={createOrder}
      >
        <div>
          <h2>Новый заказ</h2>
        </div>
        <div>
          <FormInpField labelFor="address" labelText="Адрес">
            <Input
              type="text"
              id="address"
              style={{ border: "1px solid black" }}
              value={order.address}
              required
              onChange={(e) => setOrder({ ...order, address: e.target.value })}
            />
          </FormInpField>

          <FormInpField labelFor="phone" labelText="Телефон">
            <Input
              type="text"
              id="phone"
              style={{ border: "1px solid black" }}
              value={order.phone}
              required
              maxLength={11}
              minLength={11}
              onChange={(e) => setOrder({ ...order, phone: e.target.value })}
            />
          </FormInpField>
        </div>
        <div>
          <Button type="submit" className="bg-teal-400">
            Заказать
          </Button>
        </div>
      </form>
    </div>
  );
};

export default CreateOrder;
