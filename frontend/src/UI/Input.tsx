import React from "react";

interface IInput {
  type: React.InputHTMLAttributes<HTMLImageElement>["type"];
  id?: string;
  val: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

function Input({ type = "text", id, val, onChange }: IInput): JSX.Element {
  return <input type={type} value={val} onChange={onChange} id={id} />;
}
export default Input;
