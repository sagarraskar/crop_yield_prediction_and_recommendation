import React from 'react';

import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import SeasonSelect from './SeasonSelect';
import { Box, Container, Typography, Button, TextField, Grid } from '@mui/material';

function Predict() {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    const [nitrogen, setNitrogen] = React.useState(null);
    const [phosphorus, setPhosphorus] = React.useState(null);
    const [potassium, setPotassium] = React.useState(null);
    const [rainfall, setRainfall] = React.useState(null);
    const [humidity, setHumidity] = React.useState(null);
    const [pH, setpH] = React.useState(null);
    const [temperature, settemperature] = React.useState(null);
    const [recommendation, setRecommendation] = React.useState(null);

    const recommendCrop = () => {
        const url = baseUrl + '/recommend'
        // make post request to backend
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                state: state,
                district: district,
                nitrogen: nitrogen,
                phosphorus: phosphorus,
                potassium: potassium,
                rainfall: rainfall,
                humidity: humidity,
                pH: pH,
                temperature: temperature
            })
        })
        .then(response => response.json())
        .then(data => {
            setRecommendation(data.recommendation);
        });
    }
    return (
        <div>
            <Container style={{ height: "90vh", marginTop: '2%' }} maxWidth='md'>
                <Grid container justifyContent="center" alignItems="center" spacing={2}>
                    <Grid container item xs={12} sm={5} justifyContent='center' >
                        <StateSelect />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <DistrictSelect />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <SeasonSelect />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="N"
                            label="Nitrogen"
                            type="number"
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={nitrogen}
                            onChange={(e) => setNitrogen(e.target.value)}
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="K"
                            label="Potassium"
                            type="number"
                            fullWidth
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={potassium}
                            onChange={(e) => setPotassium(e.target.value)}
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="P"
                            label="Phosphorus"
                            type="number"
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={phosphorus}
                            onChange={(e) => setPhosphorus(e.target.value)}
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="ph"
                            label="pH"
                            type="number"
                            fullWidth
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={pH}
                            onChange={(e) => setpH(e.target.value)}
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="temperature"
                            label="Temperature"
                            type="number"
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={temperature}
                            onChange={(e) => settemperature(e.target.value)}
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="humidity"
                            label="Humidity"
                            type="number"
                            fullWidth
                            variant="outlined"
                            style={{ width: '100%' }}
                            value={humidity}
                            onChange={(e) => setHumidity(e.target.value)}
                        />
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
                        <Button variant="contained" >
                            Predict
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justifyContent="center" alignItems="center" spacing={2}>
                    <Grid item>
                        <Typography textAlign='center' style={{ marginTop: 50 }}>
                            {recommendation}
                        </Typography>
                    </Grid>
                </Grid>
            </Container>

        </div>
    )
}

export default Predict;