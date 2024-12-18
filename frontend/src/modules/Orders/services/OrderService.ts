import $api from "@/http";
import { AxiosResponse } from "axios";

export default class OrderService {
  static async history(): Promise<AxiosResponse> {
    return await $api.get("/orders/history/all");
  }
}
