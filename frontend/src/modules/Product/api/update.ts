import IUpdateProduct from "../interfaces/IUpdateProduct";
import ProductClass from "../services/ProductService";

function filterEmptyFields(data: IUpdateProduct): object {
  return Object.fromEntries(
    Object.entries(data).filter(
      ([key, value]) => value != null && value !== "" && key !== "img",
    ),
  );
}

export default async function update(product: IUpdateProduct, id: number) {
  try {
    console.log(2);
    const pr = filterEmptyFields(product);
    console.log(1);
    console.log(pr);
    if (Object.keys(pr).length >= 1) {
      console.log("length");
      await ProductClass.updateProduct(pr, id);
    }
    if (product.img !== null) {
      await ProductClass.updateProductImg(product.img, id);
    }
  } catch (e) {
    console.log(e);
    throw new Error();
  }
}
