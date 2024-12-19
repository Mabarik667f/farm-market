import { useNavigate } from "react-router-dom";
import deleteProduct from "../api/deleteProduct";
import { Button } from "@/UI";

const Delete = ({ id }: { id: number }): JSX.Element => {
  const navigate = useNavigate();
  const handleDelete = async () => {
    try {
      await deleteProduct(id);
      alert("Товар был успешно удален");
      navigate("/");
    } catch {
      alert("Ошибка при удалении товара");
    }
  };
  return (
    <Button className="bg-red-500 mt-2" type="button" onClick={handleDelete}>
      Удалить
    </Button>
  );
};

export default Delete;
