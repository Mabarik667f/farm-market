import { createContext, StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import router from "@/router";
import { RouterProvider } from "react-router";
import AuthStore from "@/store/auth";

interface IAuthStore {
  store: AuthStore;
}

const store = new AuthStore();
export const Context = createContext<IAuthStore>({
  store,
});
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Context.Provider value={{ store }}>
      <RouterProvider router={router} />
    </Context.Provider>
  </StrictMode>,
);
