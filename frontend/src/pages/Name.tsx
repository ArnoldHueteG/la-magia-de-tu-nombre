import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import { createTheme, ThemeProvider } from '@mui/material/styles';
// import image from '../assets/677a33611a9910bfdc7503de78c08323.jpg'
import NameLengthMeaning from './NameLengthMeaning';
import VocalsMeaning from './VocalsMeaning';
import FirsLetterMeaning from './FirsLetterMeaning';
import LastNameMeaning from './LastNameMeaning';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import type {} from '@mui/x-date-pickers/themeAugmentation';

const theme = createTheme({
  components: {
    MuiTextField: {
      styleOverrides: {
        root: {
          '& label.MuiInputLabel-root': {
            color: 'white' // set label color to white
          },
          '& .MuiOutlinedInput-input': {
            color: 'white' // set input color to white
          },
          '& .MuiOutlinedInput-root .MuiOutlinedInput-notchedOutline': {
            borderColor: 'white' // set outline color to white
          }
        }
      }
    },
    MuiButton: {
      styleOverrides: {
        root: {
          color: 'white', // set text color to white
          borderColor: 'white', // set border color to white
          '&:hover': {
            backgroundColor: 'white', // set background color on hover to white
            color: 'black' // set text color on hover to black
          }
        }
      }
    },
    MuiSvgIcon: {
      styleOverrides: {
        root: {
          // This will change the color of the calendar icon and other SVG icons used within the DatePicker
          // color: 'white',
        },
      }
    },
    // MuiDatePicker: {
    //   styleOverrides: {
    //     root: {
    //       '& .MuiPaper-root': {
    //         backgroundColor: 'red' // set input color to white
    //       },
    //     },
    //   },
    // },
  }
});

const outputTheme = createTheme({
  components: {
    MuiTypography: {
      styleOverrides: {
        h6: {
          color: 'black', // set text color to white
          fontSize: '1.5rem' // set font size to 1.5rem
        }
      }
    }
  }
});

function NameLength() {
  const [firstName, setFirstName] = useState('');
  const [middleName, setMiddleName] = useState('');
  const [lastName, setLastName] = useState('');
  const [secondLastName, setSecondLastName] = useState('');
  const [totalLength, setTotalLength] = useState(0);
  const [fullName, setFullName] = useState({ firstName, middleName, lastName, secondLastName });
  const [birthDate, setBirthDate] = useState<Date | null>(null);

  const handleButtonClick = () => {
    const length = firstName.length + middleName.length + lastName.length + secondLastName.length;
    setTotalLength(length);
    setFullName({ firstName, middleName, lastName, secondLastName });
  };

  return (
    <ThemeProvider theme={theme}>
      <div style={{
        // height: '100vh',
        // width: '100vw',
        backgroundImage: "url(./images/677a33611a9910bfdc7503de78c08323.jpg)",
        backgroundSize: 'cover',
        backgroundRepeat: 'repeat',
        minWidth: '100vw',
        minHeight: '100vh',
        // backgroundAttachment: 'fixed',
      }}>
        <Grid container>
          {/* sx={{ m: 2 }}> */}
          <Grid item xs={12}>
            <Typography variant="h1" sx={{
              fontFamily: 'cursive',
              color: 'white',
              paddingTop: '50px',
              paddingBottom: '50px',
              fontSize: '3rem'
            }}>
              La magia de tu nombre
            </Typography>
          </Grid>
          <Grid item xs={12} sm={6} lg={3} padding={2}>
            <TextField id="outlined-basic" label="Primer Nombre" variant="outlined" focused value={firstName} onChange={(e) => setFirstName(e.target.value.toUpperCase())} fullWidth />
          </Grid>
          <Grid item xs={12} sm={6} lg={3} padding={2}>
            <TextField id="outlined-basic" label="Segundo Nombre" variant="outlined" focused value={middleName} onChange={(e) => setMiddleName(e.target.value.toUpperCase())} fullWidth />
          </Grid>
          <Grid item xs={12} sm={6} lg={3} padding={2}>
            <TextField id="outlined-basic" label="Apellido Paterno" variant="outlined" focused value={lastName} onChange={(e) => setLastName(e.target.value.toUpperCase())} fullWidth />
          </Grid>
          <Grid item xs={12} sm={6} lg={3} padding={2}>
            <TextField id="outlined-basic" label="Apellido Materno" variant="outlined" focused value={secondLastName} onChange={(e) => setSecondLastName(e.target.value.toUpperCase())} fullWidth />
          </Grid>
          <Grid item xs={12} sm={6} lg={3} padding={2}>
            <DatePicker slotProps={{
                        textField: {
                          id: "outlined-basic",
                          variant: 'outlined',
                          fullWidth: true,
                          focused: true,
                        },
                        desktopPaper: {
                          sx: {
                            backgroundColor: 'gray',
                          },
                        },
                        openPickerIcon: {
                          sx: {
                            color: 'white',
                          },
                        }
                      
                      }} label="Fecha de Nacimiento" value={birthDate} onChange={(v, c) => {
                        setBirthDate(v);
                      }} format='DD/MM/YYYY'/>
          </Grid>
          <Grid item xs={12} padding={2}>
            <Button variant="outlined" onClick={handleButtonClick}>Significado</Button>
          </Grid>
          <ThemeProvider theme={outputTheme}>
            {totalLength > 0 && birthDate &&
              <>
                <NameLengthMeaning {...fullName} />
                <VocalsMeaning {...fullName} />
                <FirsLetterMeaning {...fullName} />
                <LastNameMeaning {...fullName} />
              </>
            }
          </ThemeProvider>
        </Grid>
      </div>
    </ThemeProvider>
  );
}

export default NameLength;