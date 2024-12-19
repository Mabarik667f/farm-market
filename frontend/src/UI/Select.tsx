interface Option {
  name: string;
  value: string;
}

interface SelectProps {
  options: Option[];
  defaultValue: string;
  value: string;
  onChange: (value: string) => void;
}

const Select = ({
  options,
  defaultValue,
  value,
  onChange,
}: SelectProps): JSX.Element => {
  return (
    <select value={value} onChange={(event) => onChange(event.target.value)}>
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

export default Select;
