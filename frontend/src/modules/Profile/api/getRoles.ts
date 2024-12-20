import { RoleOut } from "@/interfaces/IUser";
import ProfileService from "../service/ProfileService";

export default async function getRoles(): Promise<RoleOut[] | undefined> {
  try {
    const response = await ProfileService.getRoles();
    return response.data;
  } catch (e) {
    console.log(e);
    return undefined;
  }
}
