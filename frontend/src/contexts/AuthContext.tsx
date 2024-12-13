import { createContext, ReactNode } from "react";
import AuthStore from "@/store/auth";

interface IAuthStore {
  store: AuthStore;
}

const store = new AuthStore();
export const AuthContext = createContext<IAuthStore>({ store });

interface AuthProvideProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProvideProps): JSX.Element => {
  return (
    <AuthContext.Provider value={{ store }}>{children}</AuthContext.Provider>
  );
};
