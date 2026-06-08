import styled from "styled-components";

export const StyledWrapper = styled.article`
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-rows: auto auto;
  width: 100%;
  height: 100%;
  overflow: hidden;
  `;

export const StyledHead = styled.p`
  margin: 0;
  padding: 0;
  font-weight: bold;
  display: grid;
  grid-template-columns: 50px 100px 550px auto;
  width: 100%;
  gap: 5px;
  span:nth-child(1) {
    width: 50px;
    overflow: hidden;
    }
  a:nth-child(2) {
    width: 100px;
    overflow: hidden;
    }
  span:nth-child(3) {
    width: 550px;
    overflow: hidden;
    }
  `;

export const StyledList = styled.ul`
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  height: 100vh;
  min-height: 0;
  overflow: scroll;
  `;

export const StyledItem = styled.li`
  display: grid;
  grid-template-columns: 50px 100px 550px auto;
  gap: 5px;
  span.test {
    background-color: blue;
    }
  span.disabled {
    background-color: red;
    }
  span:nth-child(1) {
    width: 50px;
    overflow: hidden;
    }
  span:nth-child(2) {
    width: 100px;
    overflow: hidden;
    cursor: pointer;
    }
  span:nth-child(3) {
    width: 550px;
    overflow: hidden;
    cursor: pointer;
    }
  span:nth-child(4) {
    width: 100%;
    overflow: hidden;
    }
  `;
