import React from 'react';

import { Link } from 'react-router-dom';
import { Typography, Card, CardMedia, CardActionArea, CardContent, Button, Container, Grid } from '@mui/material';

function Home() {
    return (
        <div>
            <Container style={{ height: "90vh" }} maxWidth='md'>
                <Grid container spacing={4} style={{ height: '100%' }} alignItems="center" justifyContent='space-around'>
                    <Grid item xs={12} sm={5}>
                        <Card>
                            <Link to='/predict' style={{textDecoration:'none', color:'inherit'}}>
                                <CardActionArea>
                                    <CardMedia
                                        component="img"
                                        alt="Contemplative Reptile"
                                        height="130"
                                        image="https://source.unsplash.com/random"
                                        title="Contemplative Reptile"
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            Crop Predictor
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            Predict the yield of the crop based on crop, weather conditions, and location.
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
                            </Link>
                        </Card>
                    </Grid>
                    <Grid item xs={12} sm={5}>
                        <Card>
                            <Link to='/recommend' style={{textDecoration:'none', color:'inherit'}}>
                                <CardActionArea>
                                    <CardMedia
                                        component="img"
                                        alt="Contemplative Reptile"
                                        height="130"
                                        image="https://source.unsplash.com/random"
                                        title="Contemplative Reptile"
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            Crop Recommender
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            Recommend the best crop to grow based on weather conditions and soil nutrients.
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
                            </Link>
                        </Card>
                    </Grid>
                </Grid>
            </Container>
        </div>
    );
}

export default Home;