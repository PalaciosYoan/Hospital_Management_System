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
  const [doctor, setDoctor] = useState([]);

  useEffect(() => getDoctor(), []);
  const getDoctor = () => {

    axios.post('http://127.0.0.1:5000/getDoctors', {
      queryType: 'hospital',
      hospital_name: localStorage.getItem("hospital_name")
    })
      .then(function (response) {
        console.log(response.data);
        setDoctor(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });

  };
  const classes = useStyles();
  const cards = cardStyles();

  function mapCards(doctor, index) {
    return (
      <Grid item xs={12} sm={6} md={4} key={index}>
        <Card className={classes.root} variant="outlined">
          <CardContent>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
            ></Typography>
            <Typography variant="h5" component="h2">
              <center>{doctor.name}</center>
            </Typography>
            <Typography variant="body2">
              <b>Phone Number</b>: {doctor.phone_number}
            </Typography>
            <Typography variant="body2">
              <b>Started Working</b>: {doctor.started_working}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              onClick={() => {
                console.log(doctor.name);
                localStorage.setItem("doctor_name", doctor.name);
                localStorage.setItem("d_id", doctor.d_id);
                navigate('/doctor_patient')
              }}
              size="small"
            >
              Show doctor's patient(s)
            </Button>
            <Button
              onClick={() => {
                localStorage.setItem("doctor_name", doctor.name);
                localStorage.setItem("d_id", doctor.d_id);
                navigate('/update_doctor')
              }}
              size="small"
            >
              Edit doctor
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
              <Typography variant="body2" component="p">
                <Button
                  onClick={() => {
                    navigate("/insert_doctor");
                  }}
                  size="small"
                  variant="outlined"
                >
                  Add Doctor
                </Button>
                <Button
                  onClick={() => {
                    navigate("/info");
                  }}
                  size="small"
                  variant="outlined"
                >
                  Menu
                </Button>
                <Button
                  onClick={() => {
                    navigate("/");
                  }}
                  size="small"
                  variant="outlined"
                >
                  Hub
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
        {doctor.map(mapCards)}
      </Grid>
    </div>
  );
}

export default OutlinedCard;
