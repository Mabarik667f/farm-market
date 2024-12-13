import React, { useContext, useState } from "react";
import IRegister from "../interfaces/IRegister";
import IFormInp from "@/interfaces/base/IFormInp";
import { Context } from "@/main";
import { Input, Button, FormInpField } from "@/UI";
import { useNavigate } from "react-router-dom";
import formErrors from "@/helpers/errors/formErrors";

const RegisterForm = (): JSX.Element => {
  const navigate = useNavigate();
  const { store } = useContext(Context);
  const [reg, setReg] = useState<IRegister>({
    email: "",
    username: "",
    password: "",
    password2: "",
  });
  const [errors, setErrors] = useState<IRegister>({
    email: "",
    username: "",
    password: "",
    password2: "",
  });

  const fields: IFormInp<string>[] = [
    {
      id: "login",
      label: "Логин",
      type: "text",
      value: reg.username,
      name: "username",
    },
    {
      id: "email",
      label: "Email",
      type: "email",
      value: reg.email,
      name: "email",
    },
    {
      id: "password",
      label: "Пароль",
      type: "password",
      value: reg.password,
      name: "password",
    },
    {
      id: "password2",
      label: "Повтор пароля",
      type: "password",
      value: reg.password2,
      name: "password2",
    },
  ];

  const registerEvent = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const data = await store.register(reg);
    if (typeof data === "boolean") {
      navigate("/login");
    } else {
      setReg({ ...reg, password: "", password2: "" });
      setErrors(formErrors(data));
    }
  };

  return (
    <form
      className="flex justify-center items-center flex-col h-screen"
      method="post"
      onSubmit={registerEvent}
    >
      <div>
        <h1 className="text-4xl">Регистрация</h1>
      </div>
      <div>
        {fields.map(({ id, label, type, value, name }) => (
          <FormInpField
            key={id}
            labelFor={id}
            labelText={label}
            error={errors[name as keyof IRegister]}
          >
            <Input
              type={type}
              id={id}
              style={{ border: "1px solid black" }}
              value={value}
              required
              onChange={(e) => setReg({ ...reg, [name]: e.target.value })}
            />
          </FormInpField>
        ))}
      </div>
      <div className="mt-2">
        <Button type="submit">Зарегистрироваться</Button>
      </div>
    </form>
  );
};

export default RegisterForm;
