import { AuthResponse } from "@/interfaces/response/AuthResponse";
import axios from "axios";
import Cookies from "js-cookie";

export const API_URL = "http://127.0.0.1:8000/api";

const $api = axios.create({
  withCredentials: true,
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

$api.interceptors.request.use((config) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("access")}`;
  return config;
});

$api.interceptors.response.use(
  (config) => {
    return config;
  },
  async (error) => {
    const originalRequest = error.config;
    if (
      error.response.status === 401 &&
      error.config &&
      error.config._isRetry
    ) {
      originalRequest._isRetry = true;
      try {
        const response = await axios.post<AuthResponse>(
          `${API_URL}/token/refresh`,
          { refresh: Cookies.get("refresh") },
        );
        Cookies.set("refresh", response.data.refresh);
        localStorage.setItem("access", response.data.access);
        return $api.request(originalRequest);
      } catch (e) {
        console.log(e);
      }
    }
    throw error;
  },
);

export default $api;
