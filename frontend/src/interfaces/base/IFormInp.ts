export default interface IFormInp<T = string> {
  id: string;
  label: string;
  type: string;
  value: T;
  name: string;
  placeholder?: string;
  required?: boolean;
}
