import ICategory from "@/modules/Main/interfaces/ICategory";
import { MultiSelect } from "@/UI";
import { useEffect, useState } from "react";
import getCategories from "../api/getCategories";

interface CategoriesProps {
  selected: number[];
  onChange: (selected: number[]) => void;
}

const Categories = ({ selected, onChange }: CategoriesProps): JSX.Element => {
  const [cats, setCats] = useState<ICategory[]>([]);

  useEffect(() => {
    const getCats = async () => {
      const newCats = await getCategories();
      if (newCats) {
        setCats(newCats);
      }
    };
    getCats();
  }, []);
  return (
    <div>
      <MultiSelect
        multiple
        value={selected}
        onChange={(selectedIds: number[]) => onChange(selectedIds)}
        defaultValue="Категории"
        options={cats.map((cat) => ({ value: cat.id, name: cat.name }))}
      />
    </div>
  );
};

export default Categories;
