import $api from "@/http";
import { AxiosResponse } from "axios";
import INewOrder from "../interfaces/INewOrder";

export default class CartService {
  static async cart(): Promise<AxiosResponse> {
    return await $api.get("/cart/");
  }
  static async newOrder(order: INewOrder): Promise<AxiosResponse> {
    return await $api.post("/orders/", { ...order });
  }

  static async delFromCart(cart_item_id: number): Promise<AxiosResponse> {
    return await $api.delete(`/cart/${cart_item_id}`);
  }
}
