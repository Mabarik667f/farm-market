import AuthService from "@/services/AuthService";
import { IRegister } from "@/modules/Register";
import { makeAutoObservable } from "mobx";
import Cookies from "js-cookie";
import IUser from "@/interfaces/IUser";

export default class AuthStore {
  user = {} as IUser;
  isAuth = false;
  constructor() {
    makeAutoObservable(this);
  }

  setAuth(bool: boolean) {
    this.isAuth = bool;
  }

  setUser(user: IUser) {
    this.user = user;
  }

  async login(username: string, password: string) {
    try {
      const response = await AuthService.login(username, password);
      localStorage.setItem("access", response.data.access);
      Cookies.set("refresh", response.data.refresh);
      this.setAuth(true);
      this.setUser(response.data.user);
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
}
