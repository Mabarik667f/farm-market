import { Button, FormInpField, Input } from "@/UI";
import React, { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "@/contexts/AuthContext";

function LoginForm() {
  const navigate = useNavigate();
  const [login, setLogin] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string>("");
  const { store } = useContext(AuthContext);

  const loginEvent = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    await store.login(login, password);
    if (store.isAuth) {
      navigate("/");
    } else {
      setLogin("");
      setPassword("");
      setError("Неправильный логин или пароль");
    }
  };
  return (
    <form
      className="flex justify-center items-center flex-col p-20 border-2 border-teal-400 rounded"
      method="post"
      onSubmit={loginEvent}
    >
      <div>
        <h1 className="text-4xl">Войти</h1>
        <div>{error}</div>
      </div>
      <div>
        <FormInpField labelFor="login" labelText="Логин">
          <Input
            type="text"
            id="login"
            style={{ border: "1px solid black" }}
            value={login}
            required
            onChange={(e) => setLogin(e.target.value)}
          />
        </FormInpField>
        <FormInpField labelFor="password" labelText="Пароль">
          <Input
            style={{ border: "1px solid black" }}
            type="password"
            value={password}
            id="password"
            required
            onChange={(e) => setPassword(e.target.value)}
          />
        </FormInpField>
      </div>
      <div className="mt-2">
        <Button className="border-teal-400 bg-teal-400">Войти</Button>
      </div>
    </form>
  );
}

export default LoginForm;
