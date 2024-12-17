import $api from "@/http";
import { AxiosResponse } from "axios";
import IProduct from "../interfaces/IProduct";

interface IProductsResponse {
  items: IProduct[];
  count: number;
}

export default class ProductService {
  static async getProducts(): Promise<AxiosResponse<IProductsResponse>> {
    return $api.get("/products/list/");
  }
}
