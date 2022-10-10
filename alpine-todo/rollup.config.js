import commonjs from "@rollup/plugin-commonjs";
import resolve from "@rollup/plugin-node-resolve";
import copy from 'rollup-plugin-copy'

export default 
    {
        input: "src/todo.js",
        output:[
            {
            format: "iife",
            inlineDynamicImports: true,
            file: "build/todo.js",
            }
        ],
        plugins: [
            commonjs(),
            resolve()
        ]
    };