import { AuthContext } from "@/contexts/AuthContext";
import { RoleName } from "@/interfaces/IUser";
import { useContext } from "react";
const UserData = () => {
  const { store } = useContext(AuthContext);
  const roles: Record<RoleName, { id: number; text: string }> = {
    D: { id: 1, text: "Пользователь" },
    A: { id: 2, text: "Админ" },
    S: { id: 3, text: "Продавец" },
  };

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
    </div>
  );
};

export default UserData;