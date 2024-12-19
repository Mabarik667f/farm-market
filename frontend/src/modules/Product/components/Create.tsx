import ICreateProduct from "../interfaces/ICreateProduct";
import IFormInp from "@/interfaces/base/IFormInp";
import { Button, Input, FormInpField } from "@/UI";
import React, { useState } from "react";
import create from "../api/create";
import { useNavigate } from "react-router-dom";
import Categories from "./Categories";

const Create = (): JSX.Element => {
  const [product, setProduct] = useState<ICreateProduct>({
    name: "",
    about: {},
    count: "",
    price: "",
    mass: "",
    shelf_life: "",
    category_ids: [],
    img: null,
  });
  const navigate = useNavigate();
  const createProduct = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await create(product);
      alert("Продукт был успешно создан");
      navigate("/");
    } catch {
      alert("Ошибка при создание товара");
    }
  };
  const handleCategoryChange = (selected: number[]) => {
    setProduct({ ...product, category_ids: selected });
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
        onSubmit={createProduct}
      >
        <div>
          <h1 className="text-2xl">Создать продукт</h1>
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
                  required
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
                required
                onChange={(e) =>
                  setProduct({ ...product, img: e.target.files[0] })
                }
              />
            </FormInpField>
          </div>
          <div className="border-2 border-teal-400 rounded-lg mt-4">
            <FormInpField
              key="category_ids"
              labelFor="category_ids"
              labelText="Категории"
            >
              <Categories
                selected={product.category_ids}
                onChange={handleCategoryChange}
              />
            </FormInpField>
          </div>
        </div>
        <div>
          <Button className="bg-teal-400 mt-4">Создать</Button>
        </div>
      </form>
    </div>
  );
};

export default Create;
