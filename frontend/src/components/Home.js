import React from 'react';
import { withTranslation } from 'react-i18next';

import { Link } from 'react-router-dom';
import { Typography, Card, CardMedia, CardActionArea, CardContent, Button, Container, Grid } from '@mui/material';

function Home({ t }) {
    return (
        <div>
            <Container style={{ height: "90vh" }} maxWidth='md'>
                <Grid container spacing={8} style={{ height: '100%' }} alignItems="center" justifyContent='center'>
                    <Grid item xs={12} sm={5}>
                        <Card>
                            <Link to='/predict' style={{textDecoration:'none', color:'inherit'}}>
                                <CardActionArea>
                                    <CardMedia
                                        component="img"
                                        alt="Contemplative Reptile"
                                        height="140"
                                        image="https://source.unsplash.com/random"
                                        title="Contemplative Reptile"
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            {t("predict.title")}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            {t("predict.description")}    
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
                                        height="140"
                                        image="https://source.unsplash.com/random"
                                        title="Contemplative Reptile"
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            {t("recommend.title")}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            {t("recommend.description")}    
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

export default withTranslation()(Home);