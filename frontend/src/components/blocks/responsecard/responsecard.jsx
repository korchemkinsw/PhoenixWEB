import React, { useState, useEffect } from "react";
import { CopyToClipboard } from 'react-copy-to-clipboard';
import Images from "/src/components/blocks/images/images";
import { 
  StyledResponseCard,
  StyledAccount, 
  StyledCompany, 
  StyledAddress,
  StyledGPS, 
  StyledHeadInfo, 
  StyledInfo, 
  StyledHeadPhoto, 
  } from "./styles";

export default function ResponseCard ({company}) {  
  const [text, srtText] = useState('');
  const [isCopied, setIsCopied] = useState(false);
  const onCopyText = () => {
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 1500);
  }
  const handleCopy = async (textCopy) => {
    try {
      await navigator.clipboard.writeText(textCopy)
    }
    catch (error) {
      console.error(error)
    }
  }

  const regGPS = /[5-6]\d[\.\,]\d+[\s\.\,]+[2-3]\d[\.\,]\d+/

  return (
    company.company_id && 
    <StyledResponseCard>
      <StyledAccount>{company.company_id.split('#',1)[0]}</StyledAccount>
      <StyledCompany>{company.companyname}</StyledCompany>
      <StyledAddress>{company.address}</StyledAddress>
      <StyledGPS>
        {
          company.latitude && company.longtitude && 
          <p>
            <span>Координаты:</span>
            <span>{company.latitude} {company.longtitude}</span>
            <button onClick={() => handleCopy(`${company.latitude} ${company.longtitude}`)}>copyGPS</button>
          </p>
        }
      </StyledGPS>
      {
        company.operatorprompt && company.operatorprompt.length && 
        <StyledHeadInfo>
          Информация по объекту:
          {
            regGPS.exec(company.operatorprompt) &&
            <CopyToClipboard text={regGPS.exec(company.operatorprompt)[0]} onCopy={onCopyText}>
              <button style={{'margin-left':'10px'}}>copyGPS</button>
            </CopyToClipboard>
          }
        </StyledHeadInfo>  
      }
      {
        company.operatorprompt && company.operatorprompt.length &&
        <StyledInfo>
          {company.operatorprompt}
        </StyledInfo>
      }
      {
        company.photos && company.photos.length &&    
        <StyledHeadPhoto>Фотографии объекта:</StyledHeadPhoto>
      }
      {
        company.photos && company.photos.length &&
        <div style={{'grid-area': 'photos'}}> 
          <Images images={company.photos} />
        </div>
      }
      {
        company.pictures && company.pictures.length &&    
        <StyledHeadPhoto style={{'grid-area': 'head-pictures'}}>Фотографии раздела:</StyledHeadPhoto>
      }
      {
        company.pictures && company.pictures.length &&
        <div style={{'grid-area': 'pictures'}} >
          <Images images={company.pictures} />
        </div>
      }
    </StyledResponseCard>
  )
}