import IOrder from "../interfaces/IOrder";
import OrderService from "../services/OrderService";

export default async function history(): Promise<IOrder[] | undefined> {
  try {
    const response = await OrderService.history();
    return response.data.map(
      ({ order }: { order: IOrder; profile_id: number }) => order,
    );
  } catch (e) {
    console.log(e.response.data);
    return undefined;
  }
}
