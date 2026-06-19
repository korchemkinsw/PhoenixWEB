import styled from "styled-components";

export const StyledResponseCard = styled.div`
  background: white;
  width: 98%;
  height:auto;
  margin-left: auto;
  margin-right: auto;
  display: grid;
  grid-template-areas:
      "account account company company company company"
      "address address address address address address"
      "gps gps gps gps gps gps"
      "head-inf head-inf head-inf head-inf head-inf head-inf"
      "info info info info info info"
      "head-photo head-photo head-photo head-photo head-photo head-photo"
      "photos photos photos photos photos photos"
      "head-pictures head-pictures head-pictures head-pictures head-pictures head-pictures"
      "pictures pictures pictures pictures pictures pictures"
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
  font-size: 36px;
  font-weight: bold;
  margin: 0;
  line-height: 60px;
`

export const StyledAddress = styled.p`
  grid-area: address;
  font-size: 32px;
  display: block;
  margin: 0;
  line-height: 30px;
`

export const StyledGPS = styled.p`
  grid-area: gps;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  gap: 10px;
  p {
    display: flex;
    gap: 10px;
    font-size: 28px;
    span:nth-of-type(1) {
      font-weight: bold;
    }
  }
  button {
    width: 62px;
    height: 32px;
  }
`

export const StyledHeadInfo = styled.p`
  grid-area: head-inf;
  font-weight: bold;
  button {
    width: 62px;
    height: 32px;
  }
`

export const StyledInfo = styled.textarea`
  grid-area: info;
  grid-area: info;
  resize: none;
  font-size: 28px;
  height: 250px;
`

export const StyledHeadPhoto = styled.p`
  grid-area: head-photo;
  font-weight: bold;
`