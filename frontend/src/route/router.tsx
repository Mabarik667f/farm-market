import { createBrowserRouter } from "react-router-dom";
import {
  MainPage,
  LoginPage,
  ProfilePage,
  RegisterPage,
  OrdersPage,
  CartPage,
  ProductPage,
} from "@/pages";
import App from "@/App";
import ProtectedRoute from "./ProtectedRoute";
import IsAuthRoute from "./IsAuthRoute";
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { path: "", element: <MainPage /> },
      {
        path: "orders",
        element: (
          <ProtectedRoute>
            <OrdersPage />
          </ProtectedRoute>
        ),
      },
      {
        path: "cart",
        element: (
          <ProtectedRoute>
            <CartPage />
          </ProtectedRoute>
        ),
      },
      {
        path: "profile",
        element: (
          <ProtectedRoute>
            <ProfilePage />
          </ProtectedRoute>
        ),
      },
      {
        path: "product/:id",
        element: (
          <ProtectedRoute>
            <ProductPage />
          </ProtectedRoute>
        ),
      },
    ],
  },
  {
    path: "/login",
    element: (
      <IsAuthRoute>
        <LoginPage />
      </IsAuthRoute>
    ),
  },
  {
    path: "/register",
    element: (
      <IsAuthRoute>
        <RegisterPage />
      </IsAuthRoute>
    ),
  },
]);

export default router;
