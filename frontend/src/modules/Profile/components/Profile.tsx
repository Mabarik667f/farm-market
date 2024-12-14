import LogoutBtn from "./LogoutBtn";
import UserData from "./UserData";

const Profile = (): JSX.Element => {
  return (
    <div className="flex flex-col items-center justify-center bg-teal-200 w-full h-screen">
      <UserData />
      <LogoutBtn />
    </div>
  );
};

export default Profile;
