import $api from "@/http";
import { AxiosResponse } from "axios";

export default class ProfileService {
  static async getRoles(): Promise<AxiosResponse> {
    return $api.get("/users/roles/all");
  }
}
