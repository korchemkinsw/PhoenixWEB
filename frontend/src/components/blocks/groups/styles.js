import styled from "styled-components";

export const StyledList = styled.ul`
  list-style: none;
  margin: 0;
  padding: 0;
  width: 100vw;
  display: flex;
  flex-direction: column;
  `;

export const StyledItem = styled.li`
  display: grid;
  grid-template-columns: 50px 100px 550px auto;
  gap: 5px;
  span.disabled {
    background-color: red;
    };
  `
