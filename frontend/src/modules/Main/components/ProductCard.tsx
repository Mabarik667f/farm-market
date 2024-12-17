import { useNavigate } from "react-router-dom";
import IProduct from "../interfaces/IProduct";

interface ProductCardProps {
  product: IProduct;
}

const ProductCard = ({ product }: ProductCardProps): JSX.Element => {
  const navigate = useNavigate();
  const getToProduct = (id: string) => {
    navigate(`/product/${id}`);
  };
  return (
    <div className="mb-4 p-4 text-center cursor-pointer flex flex-col items-center">
      <img
        src={`${VITE_BASE_URL}/${product.img}`}
        className="w-40 h-40 border-2 border-teal-400 rounded-lg"
        onClick={() => getToProduct(product.id.toString())}
      />
      <h5 className="text-2xl">{product.name}</h5>
      <h5 className="text-xl">{product.price} &#8381;</h5>
      <h5 className="text-wrap text-xl">{product.seller.username}</h5>
    </div>
  );
};

export default ProductCard;
