import React from "react";

interface IFormInpField {
  labelText: string;
  labelFor: string;
  children: React.ReactElement;
  className?: string;
  error?: string;
}

const FormInpField = ({
  children,
  labelText,
  labelFor,
  className,
  error,
}: IFormInpField): JSX.Element => {
  const baseClasses: string = "flex flex-col m-4";
  return (
    <div>
      <div className={`${baseClasses} ${className || ""}`}>
        <label htmlFor={labelFor}>{labelText}</label>
        <label style={{ whiteSpace: "pre-line" }}>{error}</label>
        {children}
      </div>
    </div>
  );
};

export default FormInpField;
