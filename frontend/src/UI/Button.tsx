interface IButton {
  text: string;
  type?: "button" | "submit" | "reset";
  id?: string;
  onClick?: () => void;
}

function Button({ text, type = "button", onClick }: IButton): JSX.Element {
  return (
    <button
      onClick={onClick}
      type={type}
      className="bg-blue-500 text-white py-2 px-4 rounded-md"
    >
      {text}
    </button>
  );
}

export default Button;
