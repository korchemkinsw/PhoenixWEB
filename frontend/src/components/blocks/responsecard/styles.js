import styled from "styled-components";

export const StyledResponseCard = styled.div`
  background: white;
  width: 98%;
  height:auto;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: column;
  font-size: 18px;
  line-height: 20px;
`

export const StyledCardHead = styled.div`
  display: grid;
  grid-template-columns: 110px auto;
`

export const StyledAccount = styled.p`
  font-size: 28px;
  font-weight: bold;
  margin: auto;
  width: 100px;
  line-height: 30px;
  text-align: center;
`

export const StyledCompany = styled.p`
  font-weight: bold;
  margin-top: auto;
  margin-bottom: auto;
`

export const StyledAddress = styled.p`
  display: block;
  margin: 0;
  grid-column: 1/3;
`

export const StyledGPS = styled.p`
  margin: 0;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  gap: 10px;
  p {
    display: flex;
    gap: 10px;
    span {
      margin-top: auto;
      margin-bottom: auto;
    }
    span:nth-of-type(1) {
      font-weight: bold;
    }
  }
  button {
    width: 80px;
    height: 40px;
    margin-top: auto;
    margin-bottom: auto;
  }
`

export const StyledHeadInfo = styled.p`
  font-weight: bold;
  button {
    width: 80px;
    height: 40px;
    margin-top: auto;
    margin-bottom: auto;
  }
`

export const StyledInfo = styled.textarea`
  height: 120px;
`

export const StyledHeadPhoto = styled.p`
  font-weight: bold;
`