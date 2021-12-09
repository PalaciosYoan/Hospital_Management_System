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
  const [nurse, setNurse] = useState([]);

  useEffect(() => getNurse(), []);
  const getNurse = () => {
    axios
      .post("http://127.0.0.1:5000/getRooms", {
        queryType: "nurse",
        nurse_name: localStorage.getItem("nurse_name"),
      })
      .then(function (response) {
        console.log(response.data);
        setNurse(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  const classes = useStyles();
  const cards = cardStyles();

  function deleteInfo(){
    const formInput = {};
    formInput["n_id"] = localStorage.getItem("n_id");
    formInput["r_id"] = localStorage.getItem("r_id");
    formInput["queryType"] = "delete";

    let data = { formInput };
    axios.post('http://127.0.0.1:5000/nurse_room_junc', data)
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
    console.log(data);
  }

  function mapCards(nurse, index) {
    return (
      <Grid item xs={12} sm={6} md={4} key={index}>
        <Card className={classes.root} variant="outlined">
          <CardContent  style={{textAlign: "center" }}>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
            ></Typography>
            <Typography variant="h5" component="h2">
              {nurse.room_number}
            </Typography>
            <Typography variant="body2">
              {nurse.type}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              onClick={() => {
                localStorage.setItem("nurse", nurse.name);
                navigate("/nurse_room_menu");
              }}
              size="small"
            >
              Select room
            </Button>
            <Button
                style={{ backgroundColor: "red", color: "#FFFFFF" }}
                onClick={() => {
                localStorage.setItem("r_id", nurse.r_id);
                deleteInfo();
                }}
                variant="contained"
                className={classes.button}
              >
                Delete
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
              <Button
              onClick={() => {
                navigate("/insert_nurse_room");
              }}
              size="small"
              variant="outlined"
            >
              Add Room
            </Button>
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
        {nurse.map(mapCards)}
      </Grid>
    </div>
  );
}

export default OutlinedCard;
