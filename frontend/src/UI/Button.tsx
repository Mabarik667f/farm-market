import React from "react";

type IButton = React.ButtonHTMLAttributes<HTMLButtonElement>;

const Button = ({ children, className, ...props }: IButton): JSX.Element => {
  const baseClasses = "text-white py-2 px-4 rounded-md";
  return (
    <button className={`${baseClasses} ${className || ""} `} {...props}>
      {children}
    </button>
  );
};

export default Button;
