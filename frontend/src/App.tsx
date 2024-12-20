import { NavBar } from "@/modules/NavBar";
import { Outlet } from "react-router-dom";
import { Footer } from "./modules/Footer";

const App = (): JSX.Element => {
  return (
    <div>
      <div className="top-0 left-0 w-full z-50 bg-white">
        <NavBar />
      </div>
      <div className="flex flex-col min-h-screen">
        <div className="flex-grow">
          <Outlet />
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default App;
