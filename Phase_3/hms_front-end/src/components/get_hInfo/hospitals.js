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
import { useNavigate } from "react-router-dom";

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
  const [hospital, setHospital] = useState([]);

  useEffect(() => getHospital(), []);
  const getHospital = () => {
    axios.get("http://127.0.0.1:5000/gethospital").then((response) => {
      //console.log(response);
      setHospital(response.data);
    });
  };
  const classes = useStyles();
  const cards = cardStyles();

  function mapCards(hospital, index) {
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
              {hospital.name}
            </Typography>
            <Typography variant="body2" component="p">
              {hospital.address}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              onClick={() => {
                console.log(hospital);
                localStorage.setItem("hospital_name", hospital.name);
                localStorage.setItem("hospital_address", hospital.address);
                localStorage.setItem("h_id", hospital.h_id);
                navigate("/info");
              }}
              size="small"
            >
              Select Hospital
            </Button>
            <Button
              onClick={() => {
                console.log(hospital.name);
                localStorage.setItem("hospital_name", hospital.name);
                localStorage.setItem("hospital_address", hospital.address);
                localStorage.setItem("h_id", hospital.h_id);
                navigate("/update_hospital");
              }}
              size="small"
            >
              Edit Hospital
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
                Hospital Management System
              </Typography>
              <Typography variant="body2" component="p">
              <Button
              onClick={() => {
                navigate("/insert_hospital");
              }}
              size="small"
              variant="outlined"
            >
              Add Hospital
            </Button>
            <Button
              onClick={() => {
                navigate("/all_maintenance");
              }}
              size="small"
              variant="outlined"
            >
              Show Maintenance
            </Button>
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
        {hospital.map(mapCards)}
      </Grid>
    </div>
  );
}

export default OutlinedCard;
