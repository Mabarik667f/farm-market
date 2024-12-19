export default interface ICreateProduct {
  category_ids: number[];
  shelf_life: Date;
  name: string;
  price: number;
  count: number;
  mass: number;
  img: string;
}
