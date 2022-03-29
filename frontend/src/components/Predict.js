import React from 'react';
import { baseUrl } from '../shared/baseUrl';
import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import CropSelect from './CropSelect';
import SeasonSelect from './SeasonSelect';
import { TextField, Container, Typography, Button, Grid } from '@mui/material';

function Predict() {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    const [crop, setCrop] = React.useState(null);
    const [season, setSeason] = React.useState(null);
    const [rainfall, setRainfall] = React.useState(null);
    const [prediction, setPrediction] = React.useState(null);

    const predictCrop = () => {
        const url = baseUrl + '/predict'
        // make post request to backend with no cors
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                state: state,
                district: district,
                crop: crop,
                season: season,
                rainfall: rainfall
            })
        })
            .then(response => response.json())
            .then(data => {
                setPrediction(data.estimated_yield);
            });

    }
    return (
        <div>
            <Container style={{ height: "90vh", marginTop: '2%' }} maxWidth='md'>
                <Grid container justifyContent="center" alignItems="center" spacing={2}>
                    <Grid container item xs={12} sm={5} justifyContent='center' >
                        <StateSelect state={state} setState={setState} />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <DistrictSelect state={state} district={district} setDistrict={setDistrict} />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <SeasonSelect season={season} setSeason={setSeason} />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <CropSelect crop={crop} setCrop={setCrop} />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="rainfall"
                            label="Rainfall"
                            type="number"
                            fullWidth
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={rainfall}
                            onChange={(e) => setRainfall(e.target.value)}
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
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
                            {prediction}
                        </Typography>
                    </Grid>
                </Grid>
            </Container>
        </div>
    )
}

export default Predict;