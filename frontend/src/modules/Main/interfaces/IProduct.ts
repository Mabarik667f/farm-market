import ISeller from "./ISeller";
import ICategory from "./ICategory";

export default interface IProduct {
  id: number;
  name: string;
  price: number;
  count: number;
  mass: number;
  shelf_life: Date;
  seller: ISeller;
  img: string;
  categories: Array<ICategory>;
}
