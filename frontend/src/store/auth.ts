import Cookies from "js-cookie";
import axios, { AxiosResponse } from "axios";
import AuthService from "@/services/AuthService";
import IUser from "@/interfaces/IUser";
import { IRegister } from "@/modules/Register";
import { makeAutoObservable } from "mobx";
import { API_URL } from "@/http";

export default class AuthStore {
  user = {} as IUser;
  isAuth = false;
  isLoading = false;

  constructor() {
    makeAutoObservable(this);
  }

  setAuth(bool: boolean) {
    this.isAuth = bool;
  }

  setUser(user: IUser) {
    this.user = user;
  }

  setIsLoading(bool: boolean) {
    this.isLoading = bool;
  }

  async login(username: string, password: string) {
    try {
      const response = await AuthService.login(username, password);
      Cookies.set("refresh", response.data.refresh);
      this.setInitData(response);
    } catch (e) {
      console.log(e.response.data);
    }
  }

  async register(user: IRegister): Promise<IRegister | boolean> {
    try {
      await AuthService.register(user);
      return true;
    } catch (e) {
      console.log(e.response);
      return e.response.data.detail;
    }
  }

  async logout() {
    localStorage.removeItem("access");
    Cookies.remove("refresh");
    this.setAuth(false);
    this.setUser({} as IUser);
  }

  async verifyAuth() {
    this.setIsLoading(true);
    try {
      const response = await axios.post(`${API_URL}/token/verify`, {
        token: localStorage.getItem("access"),
      });
      this.setInitData(response);
    } catch {
      await this.checkAuth();
    } finally {
      this.setIsLoading(false);
    }
  }

  async checkAuth() {
    try {
      const refresh = Cookies.get("refresh");
      const response = await axios.post(`${API_URL}/token/refresh`, {
        refresh,
      });
      this.setInitData(response);
      Cookies.set("refresh", response.data.refresh);
    } catch {
      await this.logout();
    }
  }

  setInitData(response: AxiosResponse) {
    localStorage.setItem("access", response.data.access);
    this.setAuth(true);
    const user = {
      ...response.data.user,
      roles: response.data.user.roles || [],
    };
    this.setUser(user);
  }
}
