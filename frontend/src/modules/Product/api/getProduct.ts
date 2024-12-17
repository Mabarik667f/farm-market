import IProductWithAbout from "../interfaces/IProductWithAbout";
import ProductClass from "../services/ProductService";

export default async function getProduct(
  id: number,
): Promise<IProductWithAbout | undefined> {
  try {
    const response = await ProductClass.getProduct(id);
    return response.data;
  } catch (e) {
    console.log(e);
    return undefined;
  }
}
