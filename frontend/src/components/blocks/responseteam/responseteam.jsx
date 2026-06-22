import React, { useState, useEffect } from "react";
import ResponseCard from "/src/components/blocks/responsecard/responsecard";
import { StyledWrapper, StyledTeamBlock, StyledText, StyledAlarmBlock, StyledBlockHead, StyledBlockText } from "./styles";

export default function ResponseTeam ({responseteam}) {
  return (
    <StyledWrapper>
      <StyledTeamBlock>
        <StyledText>{responseteam.description}</StyledText>
        {
          responseteam.panel_id ? (
            <StyledAlarmBlock>
              <StyledBlockHead>ТРЕВОГА</StyledBlockHead>
              <StyledBlockText><span>объект: </span>{responseteam.panel_id}</StyledBlockText>
              {
                responseteam.message && responseteam.message.length &&
                <StyledBlockText><span>раздел: </span>{responseteam.message}</StyledBlockText>
              }
              {
                responseteam.event && responseteam.event.length &&
                <StyledBlockText><span>событие: {responseteam.event}</span></StyledBlockText>
              }
            </StyledAlarmBlock>
          ) : 
          <StyledBlockText>Если ничего нет - обнови страницу или группа не отправлена в ПО "Phoenix"</StyledBlockText>
        }
      </StyledTeamBlock>
      {responseteam.company.company_id && <StyledBlockHead>Карточка объекта</StyledBlockHead>}
      {responseteam.company && <ResponseCard company = {responseteam.company} />}
    </StyledWrapper>
  )
}