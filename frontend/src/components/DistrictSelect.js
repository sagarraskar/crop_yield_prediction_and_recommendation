import * as React from 'react';

import { Autocomplete, TextField } from '@mui/material';


export default function StateSelect({ state, district, setDistrict }) {

  return (
    <Autocomplete
      id="districts-autocomplete"
      options={state?districts[state]: ['']}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label="Select District" />}
      value={district || null}
      onChange={(event, value) => setDistrict(value)}
      getOptionLabel={(option)=>option?option:""}
      style={{display:'inline-block'}}
    />
  );
}

const districts = {"Maharashtra": ['Ahmednagar', 'Pune']}
