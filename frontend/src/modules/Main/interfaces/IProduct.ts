import ISeller from "./ISeller";
import ICategory from "./ICategory";
import IBaseProduct from "./IBaseProduct";

export default interface IProduct extends IBaseProduct {
  seller: ISeller;
  categories: Array<ICategory>;
}
