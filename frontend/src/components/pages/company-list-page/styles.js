import styled from "styled-components";

export const StyledWrapper = styled.article`
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  width: 200vw;
  height: 100vw;
  overflow: hidden;
  `;

export const StyledHead = styled.p`
  margin: 0;
  padding: 0;
  font-weight: bold;
  display: flex;
  gap: 5px;
  span:nth-child(1) {
    width: 50px;
    overflow: hidden;
    }
  span:nth-child(2) {
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
  overflow: scroll;
  `;

export const StyledItem = styled.li`
  display: flex;
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
    }
  span:nth-child(3) {
    width: 550px;
    overflow: hidden;
    }
  span:nth-child(4) {
    width: 100%;
    overflow: hidden;
    }
  `;
