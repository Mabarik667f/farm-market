import { Button } from "@/UI";
import IBaseProduct from "@/modules/Main/interfaces/IBaseProduct";
import { Input } from "@/UI";
import React from "react";

interface ICartItemProps {
  product: IBaseProduct;
  count: number;
  delivery_date: string;
  isSelected: boolean;
  onSelect: (isSelected: boolean) => void;
  onRemove: () => void;
}
const CartItem = ({
  product,
  count,
  delivery_date,
  isSelected,
  onSelect,
  onRemove,
}: ICartItemProps): JSX.Element => {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onSelect(e.target.checked);
  };
  return (
    <div className="flex justify-center items-center">
      <div>
        <div className="flex">
          <div>
            <img
              src={`${VITE_BASE_URL}/${product?.img}`}
              className="w-20 mr-2"
            />
          </div>
          <div className="flex flex-col">
            <h5 className="text-2xl">{product.name}</h5>
            <div className="flex">
              <label className="mr-2">Количество:</label>
              <div>{count}</div>
            </div>
            <div className="flex">
              <label className="mr-2">Дата доставки:</label>
              <div>{delivery_date}</div>
            </div>
          </div>
        </div>
      </div>
      <div className="flex justify-center items-center">
        <Button
          className="bg-red-400 mr-2 w-7 h-7 flex items-center justify-center"
          onClick={onRemove}
        >
          &#x2715;
        </Button>
        <Input
          type="checkbox"
          checked={isSelected}
          onChange={handleChange}
          className="w-7 h-7 border-2 rounded-md cursor-pointer"
        />
      </div>
    </div>
  );
};

export default CartItem;
