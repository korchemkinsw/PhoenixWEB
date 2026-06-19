import React from "react";
import { StyledImageBlock } from "./styles";

export default function Images ({images}) {
  return (
    <StyledImageBlock>
      {
        images && images.length && images.map((image, index) =>(
          <img src={image.url} alt={`Photo${index}`} width="200" height="200" />
        ))
      }
    </StyledImageBlock>
  )
}