import React, {useState, useEffect} from "react";
import { useParams } from "react-router";
import api from "/src/api";
import ResponseCard from"/src/components/blocks/responsecard/responsecard";
import { StyledWrapper } from "./styles";

export default function ResponseCardPage () {
  const { id } = useParams()
  const [error, setError] = useState(null);
  const [card, setCard] = useState([]);
  useEffect(() => {api.getResponseCard(setCard, setError, id)},[])
  return (
    <StyledWrapper>
      <ResponseCard company = {card} />
    </StyledWrapper>
  )
}