import { useEffect, useState } from "react";
import IOrder from "../interfaces/IOrder";
import history from "../api/history";
import Order from "./Order";

const Orders = (): JSX.Element => {
  const [orders, setOrders] = useState<IOrder[]>([]);
  useEffect(() => {
    const getHistory = async () => {
      const newHistory = await history();
      if (newHistory) {
        console.log(newHistory);
        setOrders(newHistory);
      }
    };
    getHistory();
  }, []);
  if (!orders.length) {
    return (
      <div className="flex justify-center items-center text-3xl">
        Тут пока ничего нет...
      </div>
    );
  } else {
    return (
      <div className="flex flex-col justify-center items-center">
        <h1 className="text-3xl">Список заказов</h1>
        <div className="flex flex-col justify-center items-center mt-2">
          {orders.map(({ address, phone, id, created }) => (
            <Order
              key={id}
              address={address}
              phone={phone}
              created={created}
              id={id}
            />
          ))}
        </div>
      </div>
    );
  }
};

export default Orders;
