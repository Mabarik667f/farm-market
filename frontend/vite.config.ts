import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";
import dotenv from "dotenv";

dotenv.config({ path: path.resolve(__dirname, "../.env") });

const host: string = process.env.SERVER_HOST || "127.0.0.1";
const port: string = process.env.SERVER_PORT || "8000";
const protocol: string = process.env.SERVER_PROTOCOL || "http";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "@interfaces": path.resolve(__dirname, ".src/interfaces"),
      "@modules": path.resolve(__dirname, ".src/modules"),
      "@assets": path.resolve(__dirname, ".src/assets"),
      "@pages": path.resolve(__dirname, ".src/pages"),
    },
  },
});
