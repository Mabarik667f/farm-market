import AddToCart from "../interfaces/AddToCart";
import ProductClass from "../services/ProductService";

export default async function addToCart(product: AddToCart) {
  try {
    await ProductClass.addToCart(product);
    alert("Товар был успешно добавлен в корзину!");
  } catch (e) {
    console.log(e);
    alert("Ошибка");
  }
}
