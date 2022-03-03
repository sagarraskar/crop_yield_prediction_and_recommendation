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

const crops =  ['Beans & Mutter(Vegetable)', 'Cabbage', 'Drum Stick', 'Pulses total', 'Cauliflower', 'Total foodgrain', 'Bhindi', 'Tomato', 'Ginger', 'Orange', 'Pome Fruit', 'Citrus Fruit', 'Pineapple', 'Brinjal', 'Other Cereals & Millets', 'Other Vegetables', 'Cardamom', 'Mango', 'Other Fresh Fruits', 'Cowpea(Lobia)', 'Papaya', 'Moth', 'other oilseeds', 'Paddy', 'Guar seed', 'Safflower', 'Cashewnut', 'Black pepper', 'Khesari', 'Jute', 'Arecanut', 'Coconut ', 'Niger seed', 'Mesta', 'Tapioca', 'Sannhamp', 'Tobacco', 'Soyabean', 'Castor seed', 'Other  Rabi pulses', 'Dry ginger', 'Other Kharif pulses', 'Garlic', 'Banana', 'Coriander', 'Cotton(lint)', 'Horse-gram', 'Bajra', 'Ragi', 'Turmeric', 'Barley', 'Masoor', 'Sunflower', 'Linseed', 'Small millets', 'Sweet potato', 'Peas & beans (Pulses)', 'Jowar', 'Dry chillies', 'Onion', 'Gram', 'Potato', 'Groundnut', 'Arhar/Tur', 'Wheat', 'Sugarcane', 'Rapeseed &Mustard', 'Sesamum', 'Urad', 'Moong(Green Gram)', 'Maize', 'Rice']

