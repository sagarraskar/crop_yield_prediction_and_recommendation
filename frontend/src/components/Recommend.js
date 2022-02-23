import React from 'react';

import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import CropSelect from './CropSelect';
import SeasonSelect from './SeasonSelect';
import { Box, Container, Typography, Button } from '@mui/material';

function Predict() {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    const [crop, setCrop] = React.useState(null);
    const [season, setSeason] = React.useState(null);


    return (
        <div>
            <Container style={{ height: "90vh" }} maxWidth='md'>
                <Box
                    component="form"
                    sx={{
                        '& .MuiTextField-root': { m: 1, width: '25ch' },
                    }}
                    noValidate
                    autoComplete="off"
                    display="flex"
                    flexDirection="column"
                    textAlign='center'
                    justifyContent='space-evenly'
                    alignItems='center'
                    style={{height:'40%'}}
                >
                    <div>
                        <StateSelect state={state} setState={setState}/>
                        <DistrictSelect state={state} district={district} setDistrict={setDistrict}/>
                    </div>
                    <div>
                        <CropSelect crop={crop} setCrop={setCrop}/>
                        <SeasonSelect season={season} setSeason={setSeason}/>
                    </div>

                    <Button variant="contained" >
                        Predict
                    </Button>    
                </Box>
                <div style={{height: '40%', display: 'flex', flexDirection:'column', justifyContent:'center'}}>
                    <Typography textAlign='center' style={{marginTop:50}}>
                        Crop Recommended
                    </Typography>
                </div>
            </Container>
        </div>
    )
}

export default Predict;