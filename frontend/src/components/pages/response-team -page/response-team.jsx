import React, {useState, useEffect} from "react";
import { useParams } from "react-router";
import ResponseTeam from "/src/components/blocks/responseteam/responseteam";
import { StyledWrapper } from "./styles";
import api from "/src/api";

import { response_list } from "/src/mocks/group-response.js";

export default function ResponsePage () {
  const { id } = useParams()
  const [error, setError] = useState(null)
  const [teams, setTeams] = useState([])
  useEffect(() => {api.getResponseTeam(setTeams, setError)},[])

  return(
    <StyledWrapper>
      {
        !id ? teams && teams.length && teams.map((team, index) => (
          <ResponseTeam responseteam = {team} />
        )) : 
        teams && teams.filter(team => team.group_id == id).map((team, index) => (
          <ResponseTeam responseteam = {team} />
        ))
      }
    </StyledWrapper>
  )
}
  