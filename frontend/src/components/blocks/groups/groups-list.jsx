import React, {useState, useEffect} from "react";
import api from "/src/api";
import { StyledList, StyledItem } from "./styles";

export default function GroupsList ({company_id}) {
  const [error, setError] = useState(null);
  const [groupsList, setGroups] = useState([]);
  useEffect(() => {api.getGroupsCompanyList(setGroups, setError, company_id)},[])

  return (
    <StyledList>
      {
        groupsList &&
        groupsList.length &&
        groupsList.map((group, index) => (
          <StyledItem key={index}>
            <span className={group.disabled ? "disabled" : "act"}></span>
            <span>{group.group_field}</span>
            <span>{group.message}</span>
          </StyledItem>
        ))
      }
    </StyledList>
  )
}
