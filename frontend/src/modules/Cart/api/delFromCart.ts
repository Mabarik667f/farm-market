import CartService from "../services/CartServices";

export default async function delFromCart(id: number) {
  try {
    await CartService.delFromCart(id);
  } catch (e) {
    console.log(e);
  }
}
