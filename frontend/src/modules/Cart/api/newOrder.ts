import INewOrder from "../interfaces/INewOrder";
import CartService from "../services/CartServices";

export default async function newOrder(order: INewOrder) {
  try {
    await CartService.newOrder(order);
  } catch (e) {
    console.log(e);
    throw new Error();
  }
}
