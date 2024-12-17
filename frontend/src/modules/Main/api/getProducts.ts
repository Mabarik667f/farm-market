import IProduct from "../interfaces/IProduct";
import ProductService from "../services/ProductService";

export default async function getProducts(): Promise<IProduct[] | undefined> {
  try {
    const response = await ProductService.getProducts();
    return response.data.items;
  } catch (e) {
    console.log(e);
    console.log("Ошибка загрузки продуктов");
  }
}
