import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";
// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "@interfaces": path.resolve(__dirname, ".src/interfaces"),
      "@modules": path.resolve(__dirname, ".src/modules"),
      "@assets": path.resolve(__dirname, ".src/assets"),
    },
  },
});
