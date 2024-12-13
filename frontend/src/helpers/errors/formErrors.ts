export default function formErrors<T extends object>(
  data: T,
): { [K in keyof T]: string } {
  const newErrors: { [K in keyof T]: string } = {} as {
    [K in keyof T]: string;
  };
  for (const key of Object.keys(data) as (keyof T)[]) {
    let val: string = "";
    if (Array.isArray(data[key])) {
      val = data[key].join("\n");
    } else if (typeof data[key] === "string") {
      val = data[key];
    }
    newErrors[key] = val;
  }
  return newErrors;
}
