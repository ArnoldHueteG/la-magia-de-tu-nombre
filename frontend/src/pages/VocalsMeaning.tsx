import React from 'react';
import { Box, Grid, Typography } from '@mui/material/';

interface Props {
  firstName: string;
  middleName: string;
  lastName: string;
  secondLastName: string;
}

interface VocalMeaning {
  count: number;
  message: string;
}

interface VocalsMeaningResponse {
  [key: string]: VocalMeaning;
}

const VocalsMeaning: React.FC<Props> = ({ firstName, middleName }) => {
  const [vocalsMeaning, setVocalsMeaning] = React.useState<VocalsMeaningResponse>({});

  React.useEffect(() => {
    const fetchMeaning = async () => {
      const url = `${import.meta.env.VITE_API_URL}/get-vocals-meaning?firstName=${firstName}&middleName=${middleName}`;
      const response = await fetch(url);
      const data = await response.json();
      setVocalsMeaning(data);
    };
    fetchMeaning();
  }, [firstName, middleName]);

  return (
    <Box borderRadius={1} bgcolor="rgba(229, 229, 229, 0.5)" m="2rem">
      <Grid item xs={12}>
        <Typography variant="h6" style={{ textAlign: 'center' }}>
          El significado de las vocales en tu nombre:
        </Typography>
        {Object.entries(vocalsMeaning).map(([vocal, { count, message }]) => (
          <Typography key={vocal} variant="h6" style={{ textAlign: 'left' }}>
            <strong>La letra "{vocal.toUpperCase()}" aparece {count} veces en tu nombre.</strong> {message}
          </Typography>
        ))}
      </Grid>
    </Box>
  );
};

export default VocalsMeaning;