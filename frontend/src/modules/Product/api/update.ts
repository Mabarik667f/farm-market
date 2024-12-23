import IUpdateProduct from "../interfaces/IUpdateProduct";
import ProductClass from "../services/ProductService";
import $api from "@/http";

function filterEmptyFields(data: IUpdateProduct): object {
  return Object.fromEntries(
    Object.entries(data).filter(
      ([key, value]) =>
        value != null && value !== "" && key !== "img" && key !== "about",
    ),
  );
}

export default async function update(product: IUpdateProduct, id: number) {
  try {
    const pr = filterEmptyFields(product);
    if (Object.keys(pr).length >= 1) {
      await ProductClass.updateProduct(pr, id);
    }
    if (product.img !== null) {
      await ProductClass.updateProductImg(product.img, id);
    }
  } catch (e) {
    console.log(e);
    throw new Error();
  } finally {
    $api.defaults.headers["Content-Type"] = "application/json";
  }
}
