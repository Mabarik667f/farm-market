import IFormInp from "@/interfaces/base/IFormInp";
import { Button, Input, FormInpField } from "@/UI";
import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import IUpdateProduct from "../interfaces/IUpdateProduct";
import update from "../api/update";

const Update = (): JSX.Element => {
  const [product, setProduct] = useState<IUpdateProduct>({
    name: "",
    count: "",
    price: "",
    mass: "",
    shelf_life: "",
    img: null,
  });
  const navigate = useNavigate();
  const { id } = useParams();
  const updateProduct = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await update(product, id);
      alert("Продукт был успешно обновлен");
      navigate(`/product/${id}`);
    } catch {
      alert("Ошибка при обновлении товара");
    }
  };
  const fields: IFormInp<string | number | boolean | Date>[] = [
    {
      id: "name",
      label: "Название",
      type: "text",
      value: product.name,
      name: "name",
    },
    {
      id: "count",
      label: "Количество",
      type: "number",
      value: product.count,
      name: "count",
    },
    {
      id: "price",
      label: "Цена",
      type: "number",
      value: product.price,
      name: "price",
    },
    {
      id: "mass",
      label: "Масса",
      type: "number",
      value: product.mass,
      name: "mass",
    },
    {
      id: "shelf_life",
      label: "Срок годности",
      type: "date",
      value: product.shelf_life,
      name: "shelf_life",
    },
  ];
  return (
    <div className="flex justify-center items-center">
      <form
        method="post"
        className="flex justify-center items-center flex-col p-20 border-2 border-teal-400 rounded w-200"
        onSubmit={updateProduct}
      >
        <div>
          <h1 className="text-2xl">Обновить продукт</h1>
        </div>
        <div className="flex flex-col justify-center items-center">
          <div>
            {fields.map(({ id, label, type, value, name }) => (
              <FormInpField key={id} labelFor={id} labelText={label}>
                <Input
                  type={type}
                  id={id}
                  style={{ border: "1px solid black" }}
                  value={value}
                  // required
                  onChange={(e) =>
                    setProduct({ ...product, [name]: e.target.value })
                  }
                />
              </FormInpField>
            ))}
          </div>
          <div>
            <FormInpField key="img" labelFor="img" labelText="Изображение">
              <Input
                type="file"
                id="img"
                style={{ border: "1px solid black" }}
                // required
                onChange={(e) =>
                  setProduct({ ...product, img: e.target.files[0] })
                }
              />
            </FormInpField>
          </div>
        </div>
        <div>
          <Button className="bg-teal-400 mt-4">Обновить</Button>
        </div>
      </form>
    </div>
  );
};

export default Update;
