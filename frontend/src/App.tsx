import { NavBar } from "@/modules/NavBar";
import { Outlet } from "react-router-dom";

const App = (): JSX.Element => {
  return (
    <div>
      <NavBar />
      <main>
        <Outlet />
      </main>
    </div>
  );
};

export default App;
