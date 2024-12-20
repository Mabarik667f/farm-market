import LogoutBtn from "./LogoutBtn";
import UserData from "./UserData";

const Profile = (): JSX.Element => {
  return (
    <div className="flex flex-col items-center justify-center w-full h-screen">
      <UserData />
      <LogoutBtn />
    </div>
  );
};

export default Profile;
