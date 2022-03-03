import * as React from 'react';

import { Autocomplete, TextField } from '@mui/material';


export default function StateSelect({ state, setState }) {
  const [district, setDistrict] = React.useState(null);

  return (
    <Autocomplete
      id="states-autocomplete"
      options={states}
      sx={{ width: '100%'}}
      renderInput={(params) => <TextField {...params} label="Select State" />}
      value={state || null}
      onChange={(event, value) => setState(value)}
      getOptionLabel={(option)=>option?option:""}
      style={{display: 'inline-block'}}
    />
  );
}

const states = ['Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
'Dadra and Nagar Haveli', 'Goa', 'Haryana', 'Himachal Pradesh',
'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura',
'Uttar Pradesh', 'Uttarakhand'];
