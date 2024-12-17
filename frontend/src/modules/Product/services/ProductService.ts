import $api from "@/http";
import { AxiosResponse } from "axios";
import AddToCart from "../interfaces/AddToCart";

export default class ProductClass {
  static async getProduct(id: number): Promise<AxiosResponse> {
    return $api.get(`/products/${id}`);
  }

  static async addToCart(product: AddToCart): Promise<AxiosResponse> {
    return $api.post("/cart/", { ...product });
  }
}
