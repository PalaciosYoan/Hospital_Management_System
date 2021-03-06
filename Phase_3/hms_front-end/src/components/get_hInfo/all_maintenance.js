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
  const [maintenance, setMaintenance] = useState([]);

  useEffect(() => getMaintenance(), []);
  const getMaintenance = () => {

    axios.get('http://127.0.0.1:5000/getallMaintence')
      .then(function (response) {
        console.log(response.data);
        setMaintenance(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });

  };
  const classes = useStyles();
  const cards = cardStyles();

  function mapCards(maintenance, index) {
    return (
      <Grid item xs={12} sm={6} md={4} key={index}>
        <Card className={classes.root} variant="outlined">
          <CardContent>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
            ></Typography>
            <Typography variant="h5" component="h2" style={{ textAlign: "center" }}>
              {maintenance.name}
            </Typography>
            <Typography variant="body2" component="p">
              {maintenance.address}
            </Typography>
            <Typography variant="body2">
              <b>Duty</b>: {maintenance.duty}
            </Typography>
            <Typography variant="body2">
              <b>Phone Number</b>: {maintenance.phone_number}
            </Typography>
            <Typography variant="body2">
              <b>Founded</b>: {maintenance.started_working}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              onClick={() => {
                console.log(maintenance.name);
                localStorage.setItem("maintenance_name", maintenance.name);
                localStorage.setItem("maint_id", maintenance.maint_id);
                navigate('/hospital_maintenance')
              }}
              size="small"
            >
              Show hospitals they are maintaining
            </Button>
            <Button
              onClick={() => {
                console.log(maintenance.name);
                localStorage.setItem("maintenance_name", maintenance.name);
                localStorage.setItem("maint_id", maintenance.maint_id);
                navigate('/update_all_maintenance')
              }}
              size="small"
            >
              Edit maintenance
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
              <Typography variant="body2" component="p">
                <Button
                  onClick={() => {
                    navigate("/insert_maintenance_menu");
                  }}
                  size="small"
                  variant="outlined"
                >
                  Add Maintenance
                </Button>
              </Typography>
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
        {maintenance.map(mapCards)}
      </Grid>
    </div>
  );
}

export default OutlinedCard;
