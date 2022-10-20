import commonjs from "@rollup/plugin-commonjs";
import resolve from "@rollup/plugin-node-resolve";
import copy from 'rollup-plugin-copy'

export default 
    {
        input: "src/alpineobjects.js",
        output:[
            {
            format: "iife",
            inlineDynamicImports: true,
            file: "build/alpineobjects.js",
            }
        ],
        plugins: [
            commonjs(),
            resolve()
        ]
    };