import * as React from 'react';

import { Autocomplete, TextField } from '@mui/material';


export default function StateSelect({ crop, setCrop }) {

  return (
    <Autocomplete
      id="crops-autocomplete"
      options={crops}
      sx={{ width: '100%'}}
      renderInput={(params) => <TextField {...params} label="Select Crop" />}
      value={crop || null}
      onChange={(event, value) => setCrop(value)}
      getOptionLabel={(option)=>option?option:""}
      style={{display:'inline-block'}}
    />
  );
}

const crops =  ['Maize', 'Wheat']
