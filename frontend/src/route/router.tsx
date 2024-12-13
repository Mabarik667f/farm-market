import { createBrowserRouter } from "react-router-dom";
import { MainPage, LoginPage, ProfilePage, RegisterPage } from "@/pages";
import ProtectedRoute from "./ProtectedRoute";
import IsAuthRoute from "./IsAuthRoute";
const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage />,
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
  {
    path: "/profile",
    element: (
      <ProtectedRoute>
        <ProfilePage />
      </ProtectedRoute>
    ),
  },
]);

export default router;
