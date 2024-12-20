import { AuthContext } from "@/contexts/AuthContext";
import { RoleName, RoleOut } from "@/interfaces/IUser";
import { Button } from "@/UI";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import getRoles from "../api/getRoles";
const UserData = () => {
  const { store } = useContext(AuthContext);
  const navigate = useNavigate();
  const [roles, setRoles] = useState<RoleOut[]>([]);

  useEffect(() => {
    const getAllRoles = async () => {
      const newRoles = await getRoles();
      if (newRoles) {
        setRoles(newRoles);
      }
    };
    getAllRoles();
  }, []);

  if (!store.user.roles) {
    return <div>Загрузка...</div>;
  }

  const renderRole = (roleName: RoleName) => {
    const role = roles.find((r) => r.name === roleName);
    if (role) {
      return (
        <div key={role.id} className="mt-1">
          {role.description}
        </div>
      );
    } else {
      return (
        <div key={roleName} className="mt-1">
          Неизвестная роль: {roleName}
        </div>
      );
    }
  };
  return (
    <div className="flex flex-col justify-center items-center">
      <h2 className="text-3xl m-4">{store.user.username}</h2>
      <img
        src={`${VITE_MEDIA_URL}/default.jpg`}
        className="rounded-full w-44 h-44 custom-position"
      />
      <div className="flex flex-col items-center justify-center">
        <div className="flex flex-col items-center justify-center">
          <h2 className="text-xl">Роли:</h2>
          {store.user.roles.map(({ name }: { name: RoleName }) =>
            renderRole(name),
          )}
        </div>
      </div>
      {store.user.roles.some((role) => role.name === "S") && (
        <Button
          className="bg-teal-400 mt-2"
          type="button"
          onClick={() => navigate("/create-product")}
        >
          Создать продукт
        </Button>
      )}
    </div>
  );
};

export default UserData;
