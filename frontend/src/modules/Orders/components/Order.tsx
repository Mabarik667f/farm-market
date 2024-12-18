import dateFormat from "@/modules/Cart/helpers/dateFormat";
import IOrder from "../interfaces/IOrder";

const Order = ({ address, phone, id, created }: IOrder): JSX.Element => {
  return (
    <div className="flex flex-col justify-center items-center border-2 border-teal-400 rounded-lg mt-4 p-4">
      <div className="flex items-center">
        <label className="text-xl mr-2">Уникальный ID заказа:</label>
        <div>{id}</div>
      </div>
      <div className="flex items-center">
        <label className="mr-2">Ваш адрес:</label>
        <div>{address}</div>
      </div>
      <div className="flex items-center">
        <label className="mr-2">Номер телефона:</label>
        <div>{phone}</div>
      </div>
      <div className="flex items-center">
        <label className="mr-2">Дата создания заказа:</label>
        <div>{dateFormat(created)}</div>
      </div>
    </div>
  );
};

export default Order;
