import IProduct from "@/modules/Main/interfaces/IProduct";

export default interface IProductWithAbout extends IProduct {
  about: { [key: string]: string | number | boolean };
}
