import React, {useState, useEffect} from "react";
import api from "/src/api";
import { StyledWrapper, StyledHead, StyledList, StyledItem, StyledCardWrapper } from "./styles";
import GroupsList from "/src/components/blocks/groups/groups-list";
import ResponseCard from"/src/components/blocks/responsecard/responsecard";
import { groups } from "/src/mocks/groups-list";

export default function CompanyListPage () {
  const [selectedCompany, setCompany] = useState("");
  const [selectedCard, setCard] = useState("");
  const [error, setError] = useState(null);
  const [companyList, setList] = useState([]);
  useEffect(() => { 
    !companyList.length && api.getCompanyList(setList, setError) 
  }, []);
  console.log(selectedCard)
  return (
    <StyledWrapper>
      <StyledHead>
        <span>Status</span>
        <span>ID</span>
        <span>Company</span>
        <span>Address</span>
      </StyledHead>
      <StyledList>
        {
          companyList && 
          companyList.length &&
          companyList.map((item, index) => (
            <StyledItem key={index} >
              <span className={item.test ? "test" : item.disabled ? "disabled" : "act"}>  </span>
              <span onClick={() => (
                  item.company_id === selectedCompany ? setCompany(""):setCompany(item.company_id)
                )}>
                {item.company_id.split('#',1)[0]}
              </span>
              <span onClick={() => (
                  item.company_id === selectedCard ? setCard(""):setCard(item.company_id)
                )}>
                {item.companyname}
              </span>
              <span>{item.address}</span>
              {
                item.company_id === selectedCompany && 
                <GroupsList company_id = {item.company_id.replace('#',"&")} />
              }
            </StyledItem>
        ))}
      </StyledList>
      {selectedCard && (
        <StyledCardWrapper>
          <ResponseCard company = {selectedCard.replace('#',"&")} />
        </StyledCardWrapper>
      )} 
    </StyledWrapper>
  )
}
