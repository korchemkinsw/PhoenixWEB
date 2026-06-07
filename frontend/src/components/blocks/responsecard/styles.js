import styled from "styled-components";

export const StyledResponseCard = styled.article`
  position: absolute;
  top: 0;
  left: 550px;
  background: white;
  width: 1080px;
  height:100vh;
  margin-left: auto;
  margin-right: auto;
  display: grid;
  grid-template-areas:
      "account account company company company company"
      "account account address address address address"
      "account account gps gps gps gps"
      "head-inf head-inf head-inf head-inf head-inf head-inf"
      "info info info info info info"
      "head-photo head-photo head-photo head-photo head-photo head-photo"
      "photo1 photo1 photo2 photo2 photo3 photo3"
      "photo4 photo4 photo5 photo5 photo6 photo6"
      "photo7 photo7 photo8 photo8 photo9 photo9";
  overflow-y: scroll;
`

export const StyledAccount = styled.p`
  grid-area: account;
  font-size: 48px;
  font-weight: bold;
  margin: auto;
  width: 180px;
  line-height: 60px;
  text-align: center;
`

export const StyledCompany = styled.p`
  grid-area: company;
  font-size: 24px;
  font-weight: bold;
  margin: 0;
  line-height: 60px;
`

export const StyledAddress = styled.p`
  grid-area: address;
  font-size: 20px;
  display: block;
  margin: 0;
  line-height: 30px;
`

export const StyledGPS = styled.p`
  grid-area: gps;
  display: flex;
  gap: 10px;
  p {
    font-size: 18px;
    span {
      font-weight: bold;
    }
  }
`

export const StyledHeadInfo = styled.p`
  grid-area: head-inf;
  font-weight: bold;
`

export const StyledInfo = styled.textarea`
  grid-area: info;
  grid-area: info;
  resize: none;
  font-size: 18px;
  height: 250px;
`

export const StyledHeadPhoto = styled.p`
  grid-area: head-photo;
  font-weight: bold;
`

export const StyledPhoto = styled.img`
  width: 360px;
  height: 360px;
  :nth-of-type(1){
    grid-area: photo1;
  }
  :nth-of-type(2){
    grid-area: photo2;
  }
  :nth-of-type(3){
    grid-area: photo3;
  }
  :nth-of-type(4){
    grid-area: photo4;
  }
  :nth-of-type(5){
    grid-area: photo5;
  }
  :nth-of-type(6){
    grid-area: photo6;
  }
  :nth-of-type(7){
    grid-area: photo7;
  }
  :nth-of-type(8){
    grid-area: photo8;
  }
  :nth-of-type(9){
    grid-area: photo9;
  }
`