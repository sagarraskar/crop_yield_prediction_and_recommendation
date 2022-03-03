import React from 'react';
import { baseUrl } from '../shared/baseUrl';
import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import CropSelect from './CropSelect';
import SeasonSelect from './SeasonSelect';
import { Box, Container, Typography, Button, Grid } from '@mui/material';

function Predict() {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    const [crop, setCrop] = React.useState(null);
    const [season, setSeason] = React.useState(null);

    const predictCrop = () => {
        const url = baseUrl + '/predict?' + (new URLSearchParams({state: state, district: district, crop: crop, season: season})).toString();
        fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        }
        );
        
    }
    return (
        <div>
            <Container style={{ height: "90vh", marginTop: '2%' }} maxWidth='md'>
                <Grid container justifyContent="center" alignItems="center" spacing={2}>
                    <Grid container item xs={12} sm={5} justifyContent='center' >
                        <StateSelect state={state} setState={setState}/>
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <DistrictSelect state={state} district={district} setDistrict={setDistrict}/>
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <SeasonSelect season={season} setSeason={setSeason} />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <CropSelect crop={crop} setCrop={setCrop} />
                    </Grid>

                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <Button variant="contained" onClick={predictCrop}>
                            Predict
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justifyContent="center" alignItems="center" spacing={2}>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <Typography textAlign='center' style={{ marginTop: 50 }}>
                            Crop Yield Prediction
                        </Typography>
                    </Grid>
                </Grid>
            </Container>
        </div>
    )
}

export default Predict;