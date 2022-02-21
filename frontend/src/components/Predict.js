import React from 'react';

import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import { Box, Container, TextField } from '@mui/material';

function Predict() {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState('');


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
                >
                    <div>
                        <StateSelect state={state} setState={setState}/>
                        <DistrictSelect state={state} district={district} setDistrict={setDistrict}/>
                    </div>
                    
                
                </Box>
            </Container>
        </div>
    )
}

export default Predict;