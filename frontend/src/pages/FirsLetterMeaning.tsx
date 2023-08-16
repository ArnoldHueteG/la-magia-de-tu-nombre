import React from 'react';
import { Box, Grid, Typography } from '@mui/material/';

interface Props {
  firstName: string;
  middleName: string;
  lastName: string;
  secondLastName: string;
}

interface FirstLetterMeaningResponse {
  letter: string;
  message: string;
}


const FirsLetterMeaning: React.FC<Props> = ({ firstName }) => {
  const [firstLetterMeaning, setFirstLetterMeaning] = React.useState<FirstLetterMeaningResponse>({ letter: '', message: '' });
  React.useEffect(() => {
    const fetchMeaning = async () => {
      const url = `${import.meta.env.VITE_API_URL}/get-first-letter-meaning?firstName=${firstName}`;
      const response = await fetch(url);
      const data = await response.json();
      setFirstLetterMeaning(data);
    };
    fetchMeaning();
  }, [firstName]);

  return (
    <Box borderRadius={1} bgcolor="rgba(229, 229, 229, 0.5)" m="2rem">
      <Grid item xs={12}>
        <Typography variant="h6" style={{ textAlign: 'center' }}>
          El significado de la primera letra de tu nombre:
        </Typography>
        <Typography variant="h6" style={{ textAlign: 'center'}}>
        <strong>La letra "{firstLetterMeaning.letter.toUpperCase()}" significa:</strong> {firstLetterMeaning.message}
        </Typography>
      </Grid>
    </Box>
  );
};

export default FirsLetterMeaning;