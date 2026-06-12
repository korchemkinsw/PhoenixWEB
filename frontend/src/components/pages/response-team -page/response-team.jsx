import React, {useState, useEffect} from "react";
import ResponseTeam from "/src/components/blocks/responseteam/responseteam";
import { StyledWrapper } from "./styles";
import api from "/src/api";

import { response_list } from "/src/mocks/group-response.js";

export default function ResponsePage () {
  
  const [error, setError] = useState(null)
  const [teams, setTeams] = useState([])
  useEffect(() => {api.getResponseTeam(setTeams, setError)},[])

  return(
    <StyledWrapper>
      {
        teams && teams.length && teams.map((team, index) => (
          <ResponseTeam responseteam = {team} />
        ))
      }
    </StyledWrapper>
  )
}
  