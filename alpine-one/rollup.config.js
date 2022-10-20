import commonjs from "@rollup/plugin-commonjs";
import resolve from "@rollup/plugin-node-resolve";

export default {
    input: "src/my_alpine.js",
    output:[
        {
        format: "iife",
        inlineDynamicImports: true,
        file: "build/my_alpine.js",
        }
    ],
    plugins: [
        commonjs(),
        resolve()
    ]
}