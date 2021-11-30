import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import { useEffect, useState } from "react";
import axios from "axios";
import { Grid } from "@material-ui/core";

const useStyles = makeStyles({
  root: {
    minWidth: 200,
  },
  bullet: {
    display: "inline-block",
    margin: "0 2px",
    transform: "scale(0.8)",
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

function OutlinedCard() {
  const [hospital, setHospital] = useState([]);

  useEffect(() => getHospital(), []);
  const getHospital = () => {
    axios.get("http://127.0.0.1:5000/gethospital").then((response) => {
      //console.log(response);
      const h = response.data;
      console.log(h);
      setHospital(h);
    });
  };
  const classes = useStyles();

  return (
    <div>
      <center>
        <Card className={classes.root} variant="outlined">
          <CardContent>
            <Typography
              className="Hospital"
              color="textSecondary"
              gutterBottom
            ></Typography>
            <Typography variant="h5" component="h2">
              {localStorage.getItem("hospital_name")}
            </Typography>
            <Typography variant="body2" component="p">
            {localStorage.getItem("hospital_address")}
            </Typography>
          </CardContent>
        </Card>
      </center>
      &nbsp;
      <Grid
        container
        spacing={4}
        className={classes.gridContainer}
        justifyContent="center"
      >
        <Grid item xs={12} sm={6} md={4}>
          <Card className={classes.root} variant="outlined">
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                <center>Doctor</center>
              </Typography>
            </CardContent>

            <CardActions style={{ justifyContent: "center" }}>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Doctor
              </Button>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Edit Doctor
              </Button>
            </CardActions>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card className={classes.root} variant="outlined">
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                <center>Patient</center>
              </Typography>
            </CardContent>
            <CardActions style={{ justifyContent: "center" }}>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Patient
              </Button>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Edit Patient
              </Button>
            </CardActions>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card className={classes.root} variant="outlined">
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                <center>Room</center>
              </Typography>
            </CardContent>
            <CardActions style={{ justifyContent: "center" }}>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Room
              </Button>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Edit Room
              </Button>
            </CardActions>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card className={classes.root} variant="outlined">
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                <center>Nurse</center>
              </Typography>
            </CardContent>
            <CardActions style={{ justifyContent: "center" }}>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Nurse
              </Button>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Edit Nurse
              </Button>
            </CardActions>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card className={classes.root} variant="outlined">
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                <center>Maintenance</center>
              </Typography>
            </CardContent>
            <CardActions style={{ justifyContent: "center" }}>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Mainten.
              </Button>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Mainten.
              </Button>
            </CardActions>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card className={classes.root} variant="outlined">
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                <center>Maintenance</center>
              </Typography>
            </CardContent>
            <CardActions style={{ justifyContent: "center" }}>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Maintenance
              </Button>
              <Button
                onClick={() => {
                  console.log(hospital.name);
                }}
                size="small"
              >
                Select Maintenance
              </Button>
            </CardActions>
          </Card>
        </Grid>
      </Grid>
    </div>
  );
}

export default OutlinedCard;
