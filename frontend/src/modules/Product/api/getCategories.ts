import ICategory from "@/modules/Main/interfaces/ICategory";
import ProductClass from "../services/ProductService";

export default async function getCategories(): Promise<
  ICategory[] | undefined
> {
  try {
    const response = await ProductClass.getCategories();
    return response.data;
  } catch (e) {
    console.log(e);
    return undefined;
  }
}
