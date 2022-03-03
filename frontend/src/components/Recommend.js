import React from 'react';

import StateSelect from './StateSelect';
import DistrictSelect from './DistrictSelect';
import CropSelect from './CropSelect';
import SeasonSelect from './SeasonSelect';
import { Box, Container, Typography, Button, TextField, Grid } from '@mui/material';

function Predict() {
    const [state, setState] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    const [crop, setCrop] = React.useState(null);
    const [season, setSeason] = React.useState(null);


    return (
        <div>
            {/* <Container style={{ height: "90vh" }} maxWidth='md'>
                <Box
                    component="form"
                    sx={{
                        '& .MuiTextField-root': { m: 1, width: '300' },
                    }}
                    noValidate
                    autoComplete="off"
                    display="flex"
                    flexDirection="column"
                    textAlign='center'
                    justifyContent='space-evenly'
                    alignItems='center'
                    style={{ height: '40%', marginTop: '10%' }}
                >
                    <div>
                        <StateSelect state={state} setState={setState}/>
                        <DistrictSelect state={state} district={district} setDistrict={setDistrict} />
                        <CropSelect crop={crop} setCrop={setCrop} />
                        <SeasonSelect season={season} setSeason={setSeason} />
                    </div>
                    <div style={{width: '80%'}}>
                        <TextField
                            id="N"
                            label="Nitrogen"
                            type="number"
                            variant="outlined"
                            fullWidth
                            style={{ display: 'inline-block' }}
                        />
                        <TextField
                            id="N"
                            label="Phosphorus"
                            type="number"
                            variant="outlined"
                            fullWidth
                            style={{ display: 'inline-block' }}

                        />
                        <TextField
                            id="N"
                            label="Potassium"
                            type="number"
                            fullWidth
                            variant="outlined"
                            style={{ display: 'inline-block' }}
                        />
                    </div>
                    <Button variant="contained" >
                        Predict
                    </Button>
                </Box>
                <div style={{ height: '40%', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                    <Typography textAlign='center' style={{ marginTop: 50 }}>
                        Crop Recommended
                    </Typography>
                </div>
            </Container> */}
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
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="P"
                            label="Phosphorus"
                            type="number"
                            variant="outlined"
                            style={{ width: '100%' }}
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
                        />
                    </Grid>
                    <Grid container item xs={12} sm={5} justifyContent="center">
                        <TextField
                            id="temperature"
                            label="Temperature"
                            type="number"
                            variant="outlined"
                            style={{ width: '100%' }}
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
                            Recommended Crops are
                        </Typography>
                    </Grid>
                </Grid>
            </Container>

        </div>
    )
}

export default Predict;