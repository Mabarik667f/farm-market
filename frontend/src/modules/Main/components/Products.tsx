import { useEffect, useState } from "react";
import IProduct from "../interfaces/IProduct";
import getProducts from "../api/getProducts";
import ProductCard from "./ProductCard";

const Products = (): JSX.Element => {
  const [products, setProducts] = useState<Array<IProduct>>([]);
  useEffect(() => {
    const getListOfProducts = async () => {
      const newProducts = await getProducts();
      if (newProducts) {
        setProducts(newProducts);
      }
    };
    getListOfProducts();
  }, []);
  if (!products) {
    return <div>Продукты не найдены</div>;
  }
  return (
    <div>
      <div className="flex items-center justify-between flex-wrap">
        {products?.map(({ id, ...pr }) => (
          <ProductCard key={id} product={{ id, ...pr }} />
        ))}
      </div>
    </div>
  );
};

export default Products;
