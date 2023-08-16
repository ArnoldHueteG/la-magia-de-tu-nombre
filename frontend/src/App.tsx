import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Name from './pages/Name'
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Name/>
    </LocalizationProvider>
  )
}

export default App
