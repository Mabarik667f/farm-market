import ProductClass from "../services/ProductService";

export default async function deleteProduct(id: number) {
  try {
    await ProductClass.deleteProduct(id);
  } catch (e) {
    console.log(e);
    throw new Error();
  }
}
