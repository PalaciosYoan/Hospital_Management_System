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
  const [medicine, setMedicine] = useState([]);

  useEffect(() => getMedicine(), []);
  const getMedicine = () => {

    axios.post('http://127.0.0.1:5000/getMedications', {
      queryType: 'get',
      hospital_name: localStorage.getItem("hospital_name")
    })
    .then(function (response) {
      console.log(response.data);
      setMedicine(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });

  };
  const classes = useStyles();
  const cards = cardStyles();

  function mapCards(medicine, index) {
    return (
      <Grid item xs={12} sm={6} md={4} key={index}>
        <Card className={classes.root} variant="outlined">
          <CardContent>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
            ></Typography>
            <Typography variant="h5" component="h2" style={{textAlign: "center" }}>
              {medicine.name}
            </Typography>
            <Typography variant="body2">
              <b>Cost</b>: ${medicine.cost}
            </Typography>
            <Typography variant="body2">
              <b>Treatment For</b>: {medicine.treament_for}
            </Typography>
            <Typography variant="body2">
              <b>Type</b>: {medicine.type}
            </Typography>
            <Typography variant="body2">
              <b>Side Effect</b>: {medicine.side_effect}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              onClick={() => {
                localStorage.setItem("medicine_name", medicine.name);
                navigate('/patient_medication')
              }}
              size="small"
            >
              Show Patient(s) taking this Medicine
            </Button>
            <Button
              onClick={() => {
                console.log(medicine.name);
                localStorage.setItem("medicine_name", medicine.name);
                navigate('/patient_medication')
              }}
              size="small"
            >
             Edit Medicine
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
      {medicine.map(mapCards)}
    </Grid>
    </div>
  );
}

export default OutlinedCard;
