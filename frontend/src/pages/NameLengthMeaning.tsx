import React from 'react';
import { Box, Grid, Typography } from '@mui/material/';

interface Props {
  firstName: string;
  middleName: string;
  lastName: string;
  secondLastName: string;
}

const NameLengthMeaning: React.FC<Props> = ({ firstName , middleName, lastName, secondLastName }) => {
  const [meaning, setMeaning] = React.useState("");
  const [totalLength, setTotalLength] = React.useState(0);

  React.useEffect(() => {
    const fetchMeaning = async () => {
      const url = `${import.meta.env.VITE_API_URL}/get-meaning-from-length?firstName=${firstName}&middleName=${middleName}&lastName=${lastName}&secondLastName=${secondLastName}`;
      const response = await fetch(url);
      const data = await response.json();
      setMeaning(data.message);
      setTotalLength(data.totalLength);
    };
    fetchMeaning();
  }, [firstName, middleName, lastName, secondLastName]);

  return (
    <Box borderRadius={1} bgcolor="rgba(229, 229, 229, 0.5)" m="2rem">
      <Grid item xs={12}>
        <Typography variant="h6" style={{ textAlign: 'center' }}>
          El significado de la cantidad de letras de tu nombre:
        </Typography>
        <Typography variant="h6" style={{ textAlign: 'center', fontWeight: 'bold' }}>
          Tu nombre tiene {totalLength} letras
        </Typography>
        <Typography variant="h6" style={{ textAlign: 'center' }}>
          {meaning}
        </Typography>
      </Grid>
    </Box>
  );
};

export default NameLengthMeaning;