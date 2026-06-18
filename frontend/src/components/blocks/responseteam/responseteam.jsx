import React, { useState, useEffect } from "react";
import ResponseCard from "/src/components/blocks/responsecard/responsecard";
import { StyledWrapper, StyledTeamBlock, StyledText, StyledAlarmBlock } from "./styles";

export default function ResponseTeam ({responseteam}) {
  return (
    <StyledWrapper>
      <StyledTeamBlock>
        <StyledText>{responseteam.description}</StyledText>
        {
          responseteam.panel_id ? (
            <StyledAlarmBlock>
              <h3>ТРЕВОГА</h3>
              <p><span>объект: </span>{responseteam.panel_id}</p>
              <p><span>раздел: </span>{responseteam.message}</p>
              <p><span>событие: {responseteam.event}</span></p>
            </StyledAlarmBlock>
          ) : 
          <p>Если ничего нет - обнови страницу или группа не отправлена в ПО "Phoenix"</p>
        }
      </StyledTeamBlock>
      {responseteam.company.company_id && <h3>Карточка объекта</h3>}
      {responseteam.company && <ResponseCard company = {responseteam.company} />}
    </StyledWrapper>
  )
}