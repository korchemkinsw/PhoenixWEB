import React, { useState, useEffect } from "react";
import ResponseCard from "/src/components/blocks/responsecard/responsecard";
import { StyledWrapper, StyledTeamBlock, StyledText, StyledAlarmBlock } from "./styles";

export default function ResponseTeam ({responseteam}) {
  return (
    <StyledWrapper>
      <StyledTeamBlock>
        <StyledText>{responseteam.description}</StyledText>
        <StyledAlarmBlock>
          <StyledText>{responseteam.panel_id}</StyledText>
        </StyledAlarmBlock>
      </StyledTeamBlock>
      {
        responseteam.company && <ResponseCard company = {responseteam.company} />
      }
    </StyledWrapper>
  )
}