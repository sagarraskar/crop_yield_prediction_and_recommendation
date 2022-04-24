import React from 'react';

import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import SeasonSelect from './SeasonSelect';
import { Box, Container, Typography, Button, TextField, Grid } from '@mui/material';
import { withTranslation } from 'react-i18next';
import { baseUrl } from '../shared/baseUrl';

function Recommend({t, i18n}) {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    // const [season, setSeason] = React.useState(null);
    const [nitrogen, setNitrogen] = React.useState(null);
    const [phosphorus, setPhosphorus] = React.useState(null);
    const [potassium, setPotassium] = React.useState(null);
    const [rainfall, setRainfall] = React.useState(null);
    const [humidity, setHumidity] = React.useState(null);
    const [pH, setpH] = React.useState(null);
    const [temperature, settemperature] = React.useState(null);
    const [recommendation, setRecommendation] = React.useState(null);

    const en_json = require('../assets/i18n/translations/en.json');
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
            let recommendations = data.recommended_crops[0];
            let output = ""
            if (i18n.language !== 'en') {
                for(let i=0; i<3;i++) {
                    const key = Object.keys(en_json).find(key => en_json[key] === recommendations[i]);
                    recommendations[i] = t(key);
                }

            }
            setRecommendation(recommendations.join(', ').toString());
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
                        <DistrictSelect state={state} district = {district} setDistrict={setDistrict} />
                    </Grid>
                    {/* <Grid container item xs={12} sm={5} justifyContent="center">
                        <SeasonSelect season={season} setSeason={setSeason} />
                    </Grid> */}
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="N"
                            label={t('recommend.nitrogen.label')}
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
                            label={t('recommend.potassium.label')}
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
                            label={t('recommend.phosphorus.label')}
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
                            label={t('recommend.ph.label')}
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
                            label={t('recommend.temperature.label')}
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
                            label={t('recommend.humidity.label')}
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
                            label={t('recommend.rainfall.label')}
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
                        <Button variant="contained" onClick={recommendCrop}>
                            Recommend
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justifyContent="center" alignItems="center" spacing={2}>
                    <Grid item>
                        <Typography textAlign='center' style={{ marginTop: 50 }}>
                            {t('recommend.output')} : {recommendation}
                        </Typography>
                    </Grid>
                </Grid>
            </Container>

        </div>
    )
}

export default withTranslation()(Recommend);