export type RoleName = "D" | "A" | "S" | "W" | "P" | "L" | "Ag";

interface Role {
  name: RoleName;
}

export interface RoleOut extends Role {
  id: number;
  description: string;
}

export default interface IUser {
  username: string;
  img: string;
  id: number;
  roles: Role[];
}
