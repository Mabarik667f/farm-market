const Footer = (): JSX.Element => {
  return (
    <footer className="bg-teal-400 text-white py-6 mt-10">
      <div className="container mx-auto text-center">
        <div className="mb-4">
          <a href="#" className="mx-2">
            О нас
          </a>
          <a href="#" className="mx-2">
            Контакты
          </a>
          <a href="#" className="mx-2">
            Политика конфиденциальности
          </a>
          <a href="#" className="mx-2">
            Условия использования
          </a>
        </div>
        <p className="text-sm">© 2024 ООО Альфа. Все права защищены.</p>
      </div>
    </footer>
  );
};
export default Footer;
