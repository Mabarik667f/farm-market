import { createBrowserRouter } from "react-router-dom";
import { MainPage, LoginPage, ProfilePage, RegisterPage } from "@/pages";
const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage />,
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
  {
    path: "/register",
    element: <RegisterPage />,
  },
  {
    path: "/profile",
    element: <ProfilePage />,
  },
]);

export default router;
