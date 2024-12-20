import { useContext, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import getProduct from "../api/getProduct";
import { Button } from "@/UI";
import IProductWithAbout from "../interfaces/IProductWithAbout";
import ICategory from "@/modules/Main/interfaces/ICategory";
import addToCart from "../api/addToCart";
import AddToCart from "../interfaces/AddToCart";
import Delete from "./Delete";
import { AuthContext } from "@/contexts/AuthContext";

const ProductDescribe = (): JSX.Element => {
  const { id } = useParams();
  const { store } = useContext(AuthContext);
  const [product, setProduct] = useState<IProductWithAbout>(
    {} as IProductWithAbout,
  );
  const [load, setLoad] = useState<boolean>(false);
  useEffect(() => {
    const getPr = async () => {
      setLoad(false);
      const newPr = await getProduct(Number(id));
      if (newPr) {
        setProduct({ ...newPr });
      }
      setLoad(true);
    };

    getPr();
  }, []);

  const [buy, setBuy] = useState<AddToCart>({
    count: 1,
    product_id: Number(id),
  });
  const increment = () => {
    if (buy.count < product.count) {
      setBuy({ ...buy, count: buy.count + 1 });
    }
  };

  const decrement = () => {
    if (buy.count > 1) {
      setBuy({ ...buy, count: buy.count - 1 });
    }
  };

  const addProduct = async () => {
    if (!product.count) {
      setProduct({ ...product, count: 1 });
    }
    await addToCart(buy);
    setProduct({ ...product, count: product.count - buy.count });
  };

  const navigate = useNavigate();
  const handleUpdate = () => {
    navigate(`/update-product/${id}`);
  };

  if (load) {
    return (
      <div className="flex flex-col justify-center items-center mt-4">
        <img
          src={`${VITE_BASE_URL}/${product?.img}`}
          defaultValue={""}
          className="w-96 border-2 border-teal-400 rounded-lg"
        />
        <h1 className="text-3xl mt-2">{product.name}</h1>
        <div className="flex flex-col items-center justify-between">
          <div className="flex justify-between items-center">
            <label className="mr-2 font-bold">Цена:</label>
            <div>{product.price} &#8381;</div>
          </div>

          <div className="flex justify-between items-center">
            <label className="mr-2 font-bold">В наличии:</label>
            <div>{product.count}</div>
          </div>

          <div className="flex justify-between items-center">
            <label className="mr-2 font-bold">Продавец:</label>
            <div>{product.seller?.username}</div>
          </div>

          <div className="flex justify-between items-center">
            <label className="mr-2 font-bold">Продукт годен до:</label>
            <div>{product?.shelf_life?.toString()}</div>
          </div>

          <div className="flex justify-between items-center">
            <label className="mr-2 font-bold">Масса: </label>
            <div>{product.mass} г.</div>
          </div>
          {product.about &&
            Object.entries(product?.about).map(([key, value], index) => (
              <div className="flex justify-between items-center" key={index}>
                <label className="mr-2 font-bold">
                  {key
                    .toLowerCase()
                    .split(" ")
                    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
                    .join(" ")}
                  :
                </label>
                <div>{value}</div>
              </div>
            ))}

          <div className="flex flex-col justify-between items-center">
            <label className="mr-2 font-bold">Категории:</label>
            {product.categories &&
              product?.categories.map(({ name, id }: ICategory) => (
                <div
                  className="flex flex-col justify-between items-center"
                  key={id}
                >
                  <div>{name}</div>
                </div>
              ))}
          </div>
        </div>
        <div className="flex justify-center items-center m-4">
          <Button onClick={decrement} className="bg-red-500">
            <div>-</div>
          </Button>
          <h2 className="text-2xl ml-4 mr-4">{buy?.count}</h2>
          <Button onClick={increment} className="bg-teal-400">
            <div>+</div>
          </Button>
        </div>
        <Button className="bg-teal-400" onClick={addProduct}>
          В корзину
        </Button>
        {store.user.username === product.seller.username && (
          <div className="flex flex-col">
            <Button className="bg-yellow-400 mt-2" onClick={handleUpdate}>
              Обновить
            </Button>
            <Delete id={id} />
          </div>
        )}
      </div>
    );
  } else {
    return <div>Загрузка...</div>;
  }
};

export default ProductDescribe;
