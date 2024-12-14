export type RoleName = "D" | "A" | "S";

interface Role {
  name: RoleName;
}

export default interface IUser {
  username: string;
  img: string;
  id: number;
  roles: Role[];
}
