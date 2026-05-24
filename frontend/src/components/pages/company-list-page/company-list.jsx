import React, {useState, useEffect} from "react";
import api from "/src/api";
import { StyledWrapper, StyledHead, StyledList, StyledItem } from "./styles";
import GroupsList from "/src/components/blocks/groups/groups-list";
import { groups } from "/src/mocks/groups-list";

export default function CompanyListPage ({company}) {
  const [error, setError] = useState(null);
  const [selectedCompany, setCompany] = useState("");
  //selectedCompany && useEffect(() => {api.getData(api.BackUrl.company+"/"+selectedCompany, 'groups', setList, setError)}, []);
  //selectedCompany && api.getData(api.BackUrl.company+"/"+selectedCompany, 'groups', setList, setError)
  return (
    <StyledWrapper>
      {console.log(selectedCompany)}
      <StyledHead>
        <span>Status</span>
        <span>ID</span>
        <span>Company</span>
        <span>Address</span>
      </StyledHead>
      <StyledList>
        {
          company && 
          company.length &&
          company.map((item, index) => (
            <StyledItem key={index} onClick={() => (
              item.company_id === selectedCompany ? setCompany(""):setCompany(item.company_id)
            )
              }>
              <span className={item.test ? "test" : item.disabled ? "disabled" : "act"}>  </span>
              <span>{item.panel}</span>
              <span>{item.companyname}</span>
              <span>{item.address}</span>
              {
                item.company_id === selectedCompany && 
                <GroupsList groups={item.groups} />
              }
            </StyledItem>
        ))}
      </StyledList>
    </StyledWrapper>
  )
}
