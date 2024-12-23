import $api from "@/http";
import ICreateProduct from "../interfaces/ICreateProduct";
import ProductClass from "../services/ProductService";

export default async function create(product: ICreateProduct) {
  try {
    const formData = new FormData();
    formData.append("product", JSON.stringify(product));
    formData.append("file", product.img);
    await ProductClass.createProduct(formData);
  } catch (e) {
    console.log(e);
    throw new Error();
  } finally {
    $api.defaults.headers["Content-Type"] = "application/json";
  }
}
