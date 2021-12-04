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
import { useNavigate } from 'react-router-dom';

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

const cardStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

function OutlinedCard() {
  const navigate = useNavigate();
  const [hospital_maintenance, setHospital_Maintenance] = useState([]);

  useEffect(() => getHospital_Maintenance(), []);
  const getHospital_Maintenance = () => {

    axios.post('http://127.0.0.1:5000/gethospital', {
      maint_name: localStorage.getItem("maintenance_name")
    })
    .then(function (response) {
      console.log(response.data);
      setHospital_Maintenance(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });

  };
  const classes = useStyles();
  const cards = cardStyles();

  function mapCards(hospital_maintenance, index) {
    return (
      <Grid item xs={12} sm={6} md={4} key={index}>
        <Card className={classes.root} variant="outlined">
        <CardContent style={{ textAlign: "center" }}>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
            ></Typography>
            <Typography variant="h5" component="h2">
              <center>{hospital_maintenance.name}</center>
            </Typography>
            <Typography variant="body2">
            {hospital_maintenance.address}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              onClick={() => {
                console.log(hospital_maintenance.name);
                localStorage.setItem("hospital_name", hospital_maintenance.name);
                localStorage.setItem("hospital_address", hospital_maintenance.address);
                navigate('/info')
              }}
              size="small"
            >
              select hospital
            </Button>
          </CardActions>
        </Card>
      </Grid>
    );
  }
  return (
    <div>
        <div>
        <center>
        <Card className={cards.root} variant="outlined">
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
        </div>
    <Grid
      container
      spacing={4}
      className={cards.gridContainer}
      justifyContent="center"
    >
      {hospital_maintenance.map(mapCards)}
    </Grid>
    </div>
  );
}

export default OutlinedCard;
