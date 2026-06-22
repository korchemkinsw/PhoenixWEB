import React, {useState} from "react";
import { StyledImageBlock, StyledBigImage } from "./styles";

export default function Images ({images}) {
  const [url, setUrl] = useState('')
  console.log(url)
  return (
    <StyledImageBlock>
      {
        images && images.length && images.map((image, index) =>(
          <img src={image.url} alt={`Photo${index}`} width="100" height="100" onClick={() => setUrl(image.url)}/>
        ))
      }
      {
        url && 
        <StyledBigImage>
          <img src={url} alt="Photo" width="" height="" />
          <button onClick={() => setUrl('')}>X</button>
        </StyledBigImage>
      }
    </StyledImageBlock>
  )
}