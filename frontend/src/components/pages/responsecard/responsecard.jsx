import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom"
import { 
  StyledResponseCard, 
  StyledAccount, 
  StyledCompany, 
  StyledAddress,
  StyledGPS, 
  StyledHeadInfo, 
  StyledInfo, 
  StyledHeadPhoto, 
  StyledPhoto} from "./styles";

export default function ResponseCard () {
  const {company_id} = useParams()
  const [responseCard, setCard] = useState({})
  useEffect(() => {
    fetch(
      `http://127.0.0.1:8000/phoenix/company/${company_id}`,
      {
        method: 'GET',
      }
    )
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      console.log(data.length)
      setCard(data);
    });
  }, [])
  return (
    responseCard.company_id &&
    <StyledResponseCard>
      <StyledAccount>{responseCard.company_id.split('#',1)[0]}</StyledAccount>
      <StyledCompany>{responseCard.companyname}</StyledCompany>
      <StyledAddress>{responseCard.address}</StyledAddress>
      <StyledGPS>
        {responseCard.latitude && <p><span>Широта: </span>{responseCard.latitude}</p>}
        {responseCard.longtitude && <p><span>Долгота: </span>{responseCard.longtitude}</p>}
      </StyledGPS>
      <StyledHeadInfo>Информация по объекту:</StyledHeadInfo>
      <StyledInfo>{responseCard.operatorprompt}</StyledInfo>
      <StyledHeadPhoto>Фотографии объекта:</StyledHeadPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f1.jpg`} alt="Photo1" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f2.jpg`} alt="Photo2" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f3.jpg`} alt="Photo3" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f4.jpg`} alt="Photo4" width="80" height="60"></StyledPhoto>        
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f5.jpg`} alt="Photo5" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f6.jpg`} alt="Photo6" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f7.jpg`} alt="Photo7" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f8.jpg`} alt="Photo8" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${responseCard.company_id.split('#',1)[0]}_f9.jpg`} alt="Photo9" width="80" height="60"></StyledPhoto>
    </StyledResponseCard>
  )
}