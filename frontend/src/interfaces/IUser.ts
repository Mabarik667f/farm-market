interface Role {
  name: string;
}

export default interface IUser {
  username: string;
  img: string;
  id: number;
  roles: Role[];
}
