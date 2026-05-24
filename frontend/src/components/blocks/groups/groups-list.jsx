import React from "react";
import { StyledList, StyledItem } from "./styles";

export default function GroupsList ({groups}) {
  return (
    <StyledList>
      {
        groups &&
        groups.length &&
        groups.map((group, index) => (
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
