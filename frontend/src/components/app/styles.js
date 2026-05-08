import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
  html {
    height: 100%;
    }
    
  body,
  html {
    margin: 0;
    }
    
  body {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    width: 100vw;
    height: 100vw;
    overflow: hidden;
    }
    `;