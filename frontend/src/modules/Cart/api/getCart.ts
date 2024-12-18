import ICartItem from "../interfaces/ICartItem";
import CartService from "../services/CartServices";

export default async function getCart(): Promise<ICartItem[] | undefined> {
  try {
    const response = await CartService.cart();
    return response.data;
  } catch (e) {
    console.log(e);
    return undefined;
  }
}
