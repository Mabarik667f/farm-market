import { NavBar } from "@/modules/NavBar";
import { Outlet } from "react-router-dom";

const App = (): JSX.Element => {
  return (
    <div>
      <div className="top-0 left-0 w-full z-50 bg-white">
        <NavBar />
      </div>
      <Outlet />
    </div>
  );
};

export default App;
