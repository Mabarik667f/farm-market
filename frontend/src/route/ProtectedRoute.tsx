import React, { useContext, useEffect, useState } from "react";
import { AuthContext } from "@/contexts/AuthContext";
import { Navigate } from "react-router-dom";
import { observer } from "mobx-react-lite";

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute = observer(
  ({ children }: ProtectedRouteProps): JSX.Element => {
    const { store } = useContext(AuthContext);
    const [checked, setChecked] = useState<boolean>(false);
    useEffect(() => {
      if (localStorage.getItem("access") && !store.isLoading) {
        store.verifyAuth().then(() => setChecked(true));
      }
      setChecked(true);
    }, [store]);

    if (store.isLoading) {
      return <div>Загрузка...</div>;
    }
    if (!store.isAuth && checked) {
      return <Navigate to="/login" />;
    } else {
      return <>{children}</>;
    }
  },
);

export default ProtectedRoute;