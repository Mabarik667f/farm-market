interface Option {
  name: string;
  value: string;
}

interface MultiSelectProps {
  options: Option[];
  defaultValue: string;
  value: string[] | number[];
  onChange: (value: string[] | number[]) => void;
}

const MultiSelect = ({
  options,
  defaultValue,
  value,
  onChange,
}: MultiSelectProps): JSX.Element => {
  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedOptions = Array.from(event.target.selectedOptions).map(
      (option) => option.value,
    );
    onChange(selectedOptions);
  };

  return (
    <select
      multiple
      value={value}
      onChange={handleChange}
      style={{ height: "150px", width: "200px" }}
    >
      <option disabled value="">
        {defaultValue}
      </option>
      {options.map((option) => (
        <option key={option.value} value={option.value}>
          {option.name}
        </option>
      ))}
    </select>
  );
};

export default MultiSelect;
