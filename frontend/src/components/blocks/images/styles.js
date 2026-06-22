import styled from "styled-components";

export const StyledImageBlock = styled.div`
  width: 100%;
  heigth: auto;
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
`

export const StyledBigImage = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  background-color: ivory;
  img {
    width: 100vw;
    height: 100vh;
    object-fit: contain;
  }
  button {
    position: absolute;
    top: 0;
    right: 0;
    width: 30px;
    height: 30px;
    font-size: 24px;
  }
`