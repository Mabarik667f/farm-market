import React from "react";

type IForm = React.FormHTMLAttributes<HTMLFormElement>;

const Form = ({ children, ...props }: IForm): JSX.Element => {
  return <form {...props}>{children}</form>;
};

export default Form;
