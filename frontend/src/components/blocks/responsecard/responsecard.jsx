import React, { useState, useEffect } from "react";
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

export default function ResponseCard ({company}) {  
  const handleCopy = async (textCopy) => {
    try {
      await navigator.clipboard.writeText(textCopy)
    }
    catch (error) {
      console.error(error)
    }
  }
  return (
    company.company_id && 
    <StyledResponseCard>
      <StyledAccount>{company.company_id.split('#',1)[0]}</StyledAccount>
      <StyledCompany>{company.companyname}</StyledCompany>
      <StyledAddress>{company.address}</StyledAddress>
      <StyledGPS>
        {company.latitude && company.longtitude && 
        <p>
          <span>Координаты:</span>
          <span>{company.latitude} {company.longtitude}</span>
          <button onClick={() => handleCopy(`${company.latitude} ${company.longtitude}`)}>copy</button>
        </p>}
      </StyledGPS>
      <StyledHeadInfo>Информация по объекту:</StyledHeadInfo>
      <StyledInfo>
        {company.operatorprompt}
      </StyledInfo>
      <StyledHeadPhoto>Фотографии объекта:</StyledHeadPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f1.jpg`} alt="Photo1" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f2.jpg`} alt="Photo2" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f3.jpg`} alt="Photo3" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f4.jpg`} alt="Photo4" width="80" height="60"></StyledPhoto>        
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f5.jpg`} alt="Photo5" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f6.jpg`} alt="Photo6" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f7.jpg`} alt="Photo7" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f8.jpg`} alt="Photo8" width="80" height="60"></StyledPhoto>
      <StyledPhoto src={`/Photos/${company.company_id.split('#',1)[0]}_f9.jpg`} alt="Photo9" width="80" height="60"></StyledPhoto>
    </StyledResponseCard>
  )
}