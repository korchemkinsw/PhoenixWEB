import React from "react";
import { StyledWrapper, StyledHead, StyledList, StyledItem } from "./styles";

export default function CompanyListPage ({company}) {
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
        company && 
        company.length &&
        company.map((item, index) => (
          <StyledItem key={index}>
            <span className={item.test ? "test" : item.disabled ? "disabled" : "act"}>  </span>
            <span>{item.panel}</span>
            <span>{item.companyname}</span>
            <span>{item.address}</span>
          </StyledItem>
        ))}
      </StyledList>
    </StyledWrapper>
  )
}