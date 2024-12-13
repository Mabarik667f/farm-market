import React from "react";

type IInput = React.InputHTMLAttributes<HTMLInputElement>;

const Input = (props: IInput): JSX.Element => {
  return <input {...props} />;
};
export default Input;
