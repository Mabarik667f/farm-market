import axios from "axios";

export const API_URL = "http://127.0.0.1:8000/api";

const $api = axios.create({
  withCredentials: true,
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// $api.interceptors.request.use((config) => {
//   config.headers.Authorization = `Bearer ${localStorage.getItem("access")}`;
//   return config;
// });

export default $api;
