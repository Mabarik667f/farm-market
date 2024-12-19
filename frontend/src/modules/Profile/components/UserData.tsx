import { AuthContext } from "@/contexts/AuthContext";
import { RoleName } from "@/interfaces/IUser";
import { Button } from "@/UI";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";
const UserData = () => {
  const { store } = useContext(AuthContext);
  const navigate = useNavigate();
  const roles: Record<RoleName, { id: number; text: string }> = {
    D: { id: 1, text: "Пользователь" },
    A: { id: 2, text: "Админ" },
    S: { id: 3, text: "Продавец" },
  };
  console.log(store.user.roles);

  if (!store.user.roles) {
    return <div>Загрузка...</div>;
  }

  return (
    <div className="flex flex-col">
      <img
        src={`${VITE_MEDIA_URL}/default.jpg`}
        className="rounded-full w-44 h-44 custom-position"
      />
      <div className="flex flex-col items-center">
        <h2 className="text-3xl m-4">{store.user.username}</h2>
        <div className="flex flex-col items-center">
          <h2 className="text-3xl">Роли</h2>
          {store.user.roles.map(({ name }: { name: RoleName }) =>
            roles[name] ? (
              <div key={roles[name].id} className="mt-2">
                {roles[name].text}
              </div>
            ) : (
              <div key={name} className="mt-2">
                Неизвестная роль: {name}
              </div>
            ),
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
