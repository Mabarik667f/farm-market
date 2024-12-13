import React from "react";

type IInput = React.InputHTMLAttributes<HTMLInputElement>;

const Input = (props: IInput): JSX.Element => {
  return <input className="rounded-lg block w-full p-2.5" {...props} />;
};
export default Input;
