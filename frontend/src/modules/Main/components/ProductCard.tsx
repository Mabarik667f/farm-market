import IProduct from "../interfaces/IProduct";

interface ProductCardProps {
  product: IProduct;
}

const ProductCard = ({ product }: ProductCardProps): JSX.Element => {
  return (
    <div className="mb-4 p-4 text-center cursor-pointer">
      <img
        src={`${VITE_BASE_URL}/${product.img}`}
        className="w-40 h-40 border-2 border-teal-400 rounded-lg"
      />
      <h5>{product.name}</h5>
      <h5>{product.price} &#8381;</h5>
      <h5>{product.seller.username}</h5>
    </div>
  );
};

export default ProductCard;
