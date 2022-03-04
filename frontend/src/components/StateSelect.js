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

const states = ['Andaman and Nicobar Islands', 'Andhra Pradesh',
       'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
       'Chhattisgarh', 'Dadra and Nagar Haveli', 'Goa', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir ', 'Jharkhand',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana ',
       'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'];
