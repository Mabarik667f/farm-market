import $api from "@/http";
import { AxiosResponse } from "axios";
import AddToCart from "../interfaces/AddToCart";
import ICreateProduct from "../interfaces/ICreateProduct";
import IBaseProduct from "@/modules/Main/interfaces/IBaseProduct";

export default class ProductClass {
  static async getProduct(id: number): Promise<AxiosResponse> {
    return $api.get(`/products/${id}`);
  }

  static async addToCart(product: AddToCart): Promise<AxiosResponse> {
    return $api.post("/cart/", { ...product });
  }
  static async getCategories(): Promise<AxiosResponse> {
    return $api.get("/categories/");
  }
  static async createProduct(formData: FormData): Promise<AxiosResponse> {
    $api.defaults.headers["Content-Type"] = "multipart/form-data";
    return $api.post("/products/", formData);
  }

  static async updateProduct(product: IBaseProduct): Promise<AxiosResponse> {}

  static async deleteProduct(product_id: number): Promise<AxiosResponse> {
    return $api.delete(`/products/${product_id}`);
  }
}
