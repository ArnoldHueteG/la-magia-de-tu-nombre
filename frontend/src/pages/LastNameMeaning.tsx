import React from 'react';
import { Box, Grid, Typography } from '@mui/material/';

interface Props {
  firstName: string;
  middleName: string;
  lastName: string;
  secondLastName: string;
}

interface LastNameMeaningResponse {
  first_sum_operation: string;
  second_sum_operation: string;
  result: number;
  message: string;
}

const LastNameMeaning: React.FC<Props> = ({ lastName }) => {
  const [lastNameMeaning, setLastNameMeaning] = React.useState<LastNameMeaningResponse>({
    first_sum_operation: '',
    second_sum_operation: '',
    result: 0,
    message: '',
  });
  React.useEffect(() => {
    const fetchMeaning = async () => {
      const url = `${import.meta.env.VITE_API_URL}/get-lastname-meaning?lastName=${lastName}`;
      const response = await fetch(url);
      const data = await response.json();
      setLastNameMeaning(data);
    };
    fetchMeaning();
  }, [lastName]);

  return (
    <Box borderRadius={1} bgcolor="rgba(229, 229, 229, 0.5)" m="2rem">
      <Grid item xs={12}>
        <Typography variant="h6" style={{ textAlign: 'center' }}>
          El significado de tu apellido:
        </Typography>
        <Typography variant="h6" style={{ textAlign: 'center', fontWeight: 'bold' }}>
          {lastNameMeaning.first_sum_operation}
        </Typography>
        <Typography variant="h6" style={{ textAlign: 'center', fontWeight: 'bold' }}>
          {lastNameMeaning.second_sum_operation}
        </Typography>
        <Typography variant="h6" style={{ textAlign: 'center' }}>
          {lastNameMeaning.result} - {lastNameMeaning.message}
        </Typography>
      </Grid>
    </Box>
  );
};

export default LastNameMeaning;