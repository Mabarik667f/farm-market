import $api from "@/http";
import { AuthResponse } from "@/interfaces/response/AuthResponse";
import { IRegister } from "@/modules/Register";
import { AxiosResponse } from "axios";

export default class AuthService {
  static async login(
    username: string,
    password: string,
  ): Promise<AxiosResponse<AuthResponse>> {
    return $api.post<AuthResponse>("/token/pair", {
      username: username,
      password: password,
    });
  }

  static async register(user: IRegister): Promise<AxiosResponse> {
    return $api.post<AuthResponse>("/users/register", { ...user });
  }
}
