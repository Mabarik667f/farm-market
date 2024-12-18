import IBaseProduct from "@/modules/Main/interfaces/IBaseProduct";
// import ISeller from "@/modules/Main/interfaces/ISeller";

// interface IBaseProductWithSeller extends IBaseProduct {
//   seller: ISeller;
// }
export default interface ICartItem {
  product: IBaseProduct;
  id: number;
  count: number;
  delivery_date: string;
}
