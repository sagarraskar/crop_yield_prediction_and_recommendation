import * as React from 'react';

import { Autocomplete, TextField } from '@mui/material';


export default function StateSelect({ season, setSeason }) {

  return (
    <Autocomplete
      id="seasons-autocomplete"
      options={seasons}
      sx={{ width: '100%'}}
      renderInput={(params) => <TextField {...params} label="Select Season" />}
      value={season || null}
      onChange={(event, value) => setSeason(value)}
      getOptionLabel={(option)=>option?option:""}
      style={{display:'inline-block'}}
    />
  );
}

const seasons = ['Autumn', 'Summer', 'Winter', 'Kharif', 'Rabi', 'WholeYear'];
